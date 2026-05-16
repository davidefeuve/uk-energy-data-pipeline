-- Average electricity demand by year
SELECT
    EXTRACT(YEAR FROM DATETIME) AS year,
    ROUND(AVG(ENGLAND_WALES_DEMAND), 2) AS average_demand
FROM `chrome-energy-496120-j4.energy_data.energy_demand`
GROUP BY year
ORDER BY year;

-- Peak electricity demand by year
SELECT
    EXTRACT(YEAR FROM DATETIME) AS year,
    MAX(ENGLAND_WALES_DEMAND) AS peak_demand
FROM `chrome-energy-496120-j4.energy_data.energy_demand`
GROUP BY year
ORDER BY peak_demand DESC;

-- Monthly average electricity demand
SELECT
    FORMAT_DATETIME('%Y-%m', DATETIME) AS month,
    ROUND(AVG(ENGLAND_WALES_DEMAND), 2) AS average_demand
FROM `chrome-energy-496120-j4.energy_data.energy_demand`
GROUP BY month
ORDER BY month;