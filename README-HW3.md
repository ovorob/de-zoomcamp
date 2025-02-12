# de-zoomcamp

## Note: Files were downloaded using Load Yellow Taxi Data.py script (included into the repo)

## Question 1:
SELECT count(*) FROM `central-rig-448721-n2.de_dataset.yellow_tripdata_2021_full`

**Answer**
20,332,093

## Question 2:
SELECT DISTINCT count(PULocationID) FROM `central-rig-448721-n2.de_dataset.yellow_tripdata_2021_full`;

SELECT DISTINCT count(PULocationID) FROM `central-rig-448721-n2.de_dataset.yellow_tripdata_2021_ext`;

**Answer**
0 MB for the External Table and 155.12 MB for the Materialized Table


## Question 3:
SELECT `PULocationID` FROM `central-rig-448721-n2.de_dataset.yellow_tripdata_2021_full`;

SELECT `PULocationID`, `DOLocationID` FROM `central-rig-448721-n2.de_dataset.yellow_tripdata_2021_full`;

**Answer**
BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

## Question 4:
SELECT count(*) FROM `central-rig-448721-n2.de_dataset.yellow_tripdata_2021_full` WHERE fare_amount=0;

**Answer**
8,333

## Question 5:
CREATE OR REPLACE TABLE `central-rig-448721-n2.de_dataset.yellow_tripdata_2021_full_optimised` 
PARTITION BY
  DATE(`tpep_dropoff_datetime`) 
  CLUSTER BY `VendorID` AS
SELECT * FROM `central-rig-448721-n2.de_dataset.yellow_tripdata_2021_ext`

**Answer**
Partition by tpep_dropoff_datetime and Cluster on VendorID

## Question 6:
SELECT DISTINCT `VendorID` FROM `central-rig-448721-n2.de_dataset.yellow_tripdata_2021_full_optimised` WHERE DATE(`tpep_dropoff_datetime`) BETWEEN '2024-03-01' AND '2024-03-15';

SELECT DISTINCT `VendorID` FROM `central-rig-448721-n2.de_dataset.yellow_tripdata_2021_full` WHERE DATE(`tpep_dropoff_datetime`) BETWEEN '2024-03-01' AND '2024-03-15';

**Answer**
310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

## Question 7:
**Answer**
GCP Bucket

## Question 8:
**Answer**
False

## Question 9:
**Answer**
0 bytes as materialised table cashes data