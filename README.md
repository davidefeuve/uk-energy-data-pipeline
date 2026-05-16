# UK Energy Data Engineering Pipeline

End-to-end ETL and cloud data engineering pipeline using Python, SQLite and Google BigQuery.

This project demonstrates a complete data engineering workflow using UK electricity demand data from the National Energy System Operator (NESO).

The pipeline automates:

* Raw data ingestion
* Data validation
* Processed data export
* SQLite database loading
* Google BigQuery cloud upload
* SQL analytical querying

---

# Project Architecture

```text
Raw CSV Files
       ↓
Data Ingestion
       ↓
Validation Checks
       ↓
Processed Dataset Export
       ↓
SQLite Database Load
       ↓
Google BigQuery Upload
       ↓
Cloud SQL Analysis
```

---

# Technologies Used

| Technology      | Purpose                            |
| --------------- | ---------------------------------- |
| Python          | ETL pipeline development           |
| pandas          | Data transformation and validation |
| SQLite          | Local relational database          |
| Google BigQuery | Cloud data warehouse               |
| SQL             | Data querying and aggregation      |
| Git/GitHub      | Version control                    |

---

# Project Structure

```text
uk-energy-data-pipeline/
│
├── Credentials/
├── Data/
│   ├── Raw/
│   └── Processed/
│
├── Notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_validation.ipynb
│   ├── 03_sqlite_load.ipynb
│   └── 04_bigquery_upload.ipynb
│
├── Outputs/
├── Screenshots/
├── SQL/
│   └── bigquery_analysis_queries.sql
│
├── SRC/
│   └── run_pipeline.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# ETL Pipeline Workflow

## 1. Data Ingestion

The pipeline automatically:

* Detects raw CSV files
* Reads all electricity demand datasets
* Combines them into a unified dataframe

## 2. Data Validation

Validation checks include:

* Missing value detection
* Duplicate row checks
* Negative demand validation
* Dataset integrity checks

## 3. Processed Data Export

The cleaned dataset is exported as:

```text
combined_energy_demand.csv
```

## 4. SQLite Database Loading

The processed dataset is automatically loaded into:

```text
energy_pipeline.db
```

## 5. BigQuery Cloud Upload

The pipeline uploads the dataset into:

```text
chrome-energy-496120-j4.energy_data.energy_demand
```

---

# Example SQL Queries

Example BigQuery analytical queries include:

* Average electricity demand by year
* Peak electricity demand by year
* Monthly average electricity demand

Example:

```sql
SELECT
    EXTRACT(YEAR FROM DATETIME) AS year,
    ROUND(AVG(ENGLAND_WALES_DEMAND), 2) AS average_demand
FROM `chrome-energy-496120-j4.energy_data.energy_demand`
GROUP BY year
ORDER BY year;
```

---

# Running the Pipeline

Run the full automated ETL pipeline:

```bash
python SRC/run_pipeline.py
```

The pipeline will:

1. Load raw datasets
2. Validate data quality
3. Save processed outputs
4. Load SQLite database
5. Upload data to BigQuery

---

# Future Improvements

Potential future enhancements include:

* Logging improvements
* Error handling
* Scheduling/orchestration
* Docker containerisation

---

# Author

David Fernandez

End-to-end ETL and cloud data engineering pipeline using Python, SQLite and Google BigQuery.
