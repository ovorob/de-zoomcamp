### DBT project is in 04-dbt-homework


### Question 1
select * from dtc_zoomcamp_2025.raw_nyc_tripdata.ext_green_taxi

### Question 2
pickup_datetime >= CURRENT_DATE - INTERVAL '{{ var("days_back", env_var("DAYS_BACK", "30")) }}' DAY

### Question 3
dbt run --select models/staging/+

### Question 4
- Setting a value for DBT_BIGQUERY_TARGET_DATASET env var is mandatory, or it'll fail to compile
- When using core, it materializes in the dataset defined in DBT_BIGQUERY_TARGET_DATASET
- When using stg, it materializes in the dataset defined in DBT_BIGQUERY_STAGING_DATASET, or defaults to DBT_BIGQUERY_TARGET_DATASET
- When using staging, it materializes in the dataset defined in DBT_BIGQUERY_STAGING_DATASET, or defaults to DBT_BIGQUERY_TARGET_DATASET

### Question 5
green: {best: 2020/Q1, worst: 2020/Q2}, yellow: {best: 2020/Q1, worst: 2020/Q2}

### Question 6
SELECT * FROM `central-rig-448721-n2.dbt_ovorobiov.fct_taxi_trips_monthly_fare_p95` where pickup_year=2020 and pickup_month=4

