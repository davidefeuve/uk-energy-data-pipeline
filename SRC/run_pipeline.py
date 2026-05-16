"""
UK Energy Data Engineering Pipeline

This script performs the complete ETL pipeline workflow:

1. Read raw CSV files
2. Combine datasets
3. Perform validation checks
4. Save processed dataset
5. Load data into SQLite
6. Upload data to Google BigQuery
"""

import pandas as pd
import sqlite3
from pathlib import Path
from google.cloud import bigquery

# Define project paths
RAW_DATA_PATH = Path("Data/Raw")
PROCESSED_DATA_PATH = Path("Data/Processed")
SQLITE_DATABASE_PATH = Path("Data/energy_pipeline.db")
CREDENTIALS_PATH = Path("Credentials/chrome-energy-496120-j4-299aaa8130ba.json")

def load_raw_data(raw_data_path: Path) -> pd.DataFrame:
    """Read and combine all raw CSV files from the raw data folder."""

    csv_files = list(raw_data_path.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError("No CSV files found in the raw data folder.")

    df_list = []

    for file in csv_files:
        df = pd.read_csv(file)
        df_list.append(df)

    combined_df = pd.concat(df_list, ignore_index=True)

    return combined_df

def validate_data(df: pd.DataFrame) -> None:
    """Perform basic validation checks on the dataset."""

    missing_values = df.isnull().sum()
    missing_columns = missing_values[missing_values > 0]

    print("\nColumns with missing values:")

    if missing_columns.empty:
        print("No missing values detected.")
    else:
        print(missing_columns)

    duplicate_rows = df.duplicated().sum()
    print(f"\nDuplicate rows: {duplicate_rows}")

    negative_demand = (
        df["ENGLAND_WALES_DEMAND"] < 0
    ).sum()
    print(f"Negative demand records: {negative_demand}")

def save_processed_data(
    df: pd.DataFrame,
    output_path: Path
) -> None:
    """Save processed dataset to CSV."""

    output_path.mkdir(parents=True, exist_ok=True)

    output_file = output_path / "combined_energy_demand.csv"

    df.to_csv(output_file, index=False)

    print(
        f"\nProcessed dataset saved successfully: "
        f"{output_file}"
    )

def load_to_sqlite(
    df: pd.DataFrame,
    database_path: Path
) -> None:
    """Load dataset into SQLite database."""

    connection = sqlite3.connect(database_path)

    df.to_sql(
        "energy_demand",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print(
        f"\nDataset loaded successfully into SQLite: "
        f"{database_path}"
    )

def upload_to_bigquery(
    df: pd.DataFrame,
    credentials_path: Path
) -> None:
    """Upload dataset to Google BigQuery."""

    client = bigquery.Client.from_service_account_json(credentials_path)
    table_id = ("chrome-energy-496120-j4.energy_data.energy_demand")
    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()

    print(
        f"\nDataset uploaded successfully to BigQuery: "
        f"{table_id}"
    )

raw_df = load_raw_data(RAW_DATA_PATH)

print(
    f"Raw data loaded successfully: {raw_df.shape[0]:,} rows "
    f"and {raw_df.shape[1]} columns."
)

validate_data(raw_df)
save_processed_data(raw_df, PROCESSED_DATA_PATH)
load_to_sqlite(raw_df, SQLITE_DATABASE_PATH)
upload_to_bigquery(raw_df, CREDENTIALS_PATH)