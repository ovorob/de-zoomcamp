# de-zoomcamp

## Question 1:
- docker run -it python:3.12.8 bash
- pip3 --version
-> pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)

## Question 2:

db:5432

**Prepare Postgres**
Run docker compose: 
docker-compose up

Build image and run the container: 
docker build . -t test_ingest

docker run -it \
    --network=de-zoomcamp_default \
    test_ingest \
        --user=root \
        --password=root \
        --host=pgdatabase \
        --port=5432 \
        --db=test_db \
        --table=yellow_trips \
        --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz" \
        --zones_url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"

## Question 3:

### 3.1
**Trip Distance up to 1 mile**
SELECT COUNT(*) FROM yellow_trips  WHERE DATE(lpep_pickup_datetime)>='2019-10-01' AND DATE(lpep_dropoff_datetime)<'2019-11-01' AND trip_distance<=1

**Answer** 
104802

### 3.2
**In between 1 (exclusive) and 3 miles (inclusive)**
SELECT COUNT(*) FROM yellow_trips  WHERE 
	(DATE(lpep_pickup_datetime)>='2019-10-01' AND 
	DATE(lpep_dropoff_datetime)<'2019-11-01') AND 
	(trip_distance>1 AND trip_distance<=3)

**Answer** 
198924

### 3.3
**In between 3 (exclusive) and 7 miles (inclusive)**
SELECT COUNT(*) FROM yellow_trips  WHERE 
	(DATE(lpep_pickup_datetime)>='2019-10-01' AND 
	DATE(lpep_dropoff_datetime)<'2019-11-01') AND 
	(trip_distance>3 AND trip_distance<=7)

**Answer** 
109603

### 3.4
**In between 7 (exclusive) and 10 miles (inclusive)**
SELECT COUNT(*) FROM yellow_trips  WHERE 
	(DATE(lpep_pickup_datetime)>='2019-10-01' AND 
	DATE(lpep_dropoff_datetime)<'2019-11-01') AND 
	(trip_distance>7 AND trip_distance<=10)

**Answer** 
27678

### 3.5
**Over 10 milese**
SELECT COUNT(*) FROM yellow_trips  WHERE 
	(DATE(lpep_pickup_datetime)>='2019-10-01' AND 
	DATE(lpep_dropoff_datetime)<'2019-11-01') AND 
	trip_distance>10

**Answer** 
35189

## Question 4:
SELECT DATE(lpep_pickup_datetime) as pickup,
		MAX(trip_distance) as distance
FROM yellow_trips  
GROUP BY 1 ORDER BY distance DESC

**Answer**
2019-10-31

## Question 5:
SELECT
	"Borough",
	"Zone",
	total
FROM 
	(SELECT "PULocationID",
	SUM(total_amount) as total
	FROM yellow_trips
	WHERE DATE(lpep_pickup_datetime)='2019-10-18'
	GROUP BY 1) as ty 
JOIN route_map as rm
ON ty."PULocationID"=rm."LocationID"
WHERE total>=13000
ORDER BY total DESC

**Answer**
East Harlem North, East Harlem South, Morningside Heights

## Question 6:
SELECT 
	pickup."Zone" as pickup_zone,
	dropof."Zone" as dropof_zone,
	yt.tip_amount
FROM yellow_trips yt
	JOIN route_map pickup
	ON yt."PULocationID"=pickup."LocationID"
	JOIN route_map dropof
	ON yt."DOLocationID"=dropof."LocationID"
WHERE (DATE(lpep_pickup_datetime)>='2019-10-01' AND 
	DATE(lpep_dropoff_datetime)<'2019-11-01') AND 
	pickup."Zone"='East Harlem North'
ORDER BY tip_amount DESC

**Answer**
JFK Airport


