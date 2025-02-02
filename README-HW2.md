# de-zoomcamp

## Note: Kestra yaml file was included into the repo with the name - dataset_gcp.yml, also Kestra was added to the main compose-file.

## Question 1:
128.3 MB

## Question 2:
green_tripdata_2020-04.csv

## Question 3:
SELECT COUNT(*) FROM `central-rig-448721-n2.de_dataset.yellow_tripdata` WHERE filename LIKE '%tripdata_2020%'

**Answer**
24,648,499

## Question 4:
SELECT COUNT(*) FROM `central-rig-448721-n2.de_dataset.green_tripdata` WHERE filename LIKE '%tripdata_2020%'

**Answer**
1,734,051

## Question 5:
SELECT COUNT(*) FROM `central-rig-448721-n2.de_dataset.yellow_tripdata` WHERE filename LIKE '%tripdata_2021-03%'

**Answer**
1,925,152

## Question 6:
Add a timezone property set to America/New_York in the Schedule trigger configuration