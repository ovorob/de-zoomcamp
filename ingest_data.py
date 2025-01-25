#!/usr/bin/env python
# coding: utf-8
import os
import pandas as pd
from sqlalchemy import create_engine
from time import time
import pyarrow.parquet as pq
import argparse

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table = params.table
    url = params.url
    zones_url = params.zones_url
    taxi_data_gz = 'output.csv.gz'
    taxi_data = 'output.csv'
    map_csv = 'map.csv'

    #download CSV
    os.system(f'wget {url} -O {taxi_data_gz}')
    os.system(f'wget {zones_url} -O {map_csv}')

    os.system(f'gzip -d {taxi_data_gz}')

    df_taxi_iter = pd.read_csv(taxi_data, iterator=True, chunksize=50000)
    df = next(df_taxi_iter)

    df_locations_csv = pd.read_csv(map_csv)

    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    df_locations_csv.to_sql(name='route_map', con=engine, if_exists='replace')
    print(f'Mapped was added to the table, total amount of lines: {len(df_locations_csv)}!')

    print(pd.io.sql.get_schema(df, table, con=engine))
    df.head(0).to_sql(name=table, con=engine, if_exists="replace")
    df.to_sql(name=table, con=engine, if_exists="append")

    number = 50000
    total_time = 0
    for batch in df_taxi_iter:
        start_time = time()
        batch.lpep_dropoff_datetime = pd.to_datetime(batch.lpep_dropoff_datetime)
        batch.lpep_pickup_datetime = pd.to_datetime(batch.lpep_pickup_datetime)
        batch.to_sql(name=table, con=engine, if_exists="append")
        end_time = time()
        total_time = int(total_time + (end_time - start_time))
        number += 50000
        print(f'Another batch completed... Time spent - {total_time} sec; Completed {number}!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest data in to Postgres DB')
    parser.add_argument('--user', help='User to the DB')
    parser.add_argument('--password', help='Password to the DB')
    parser.add_argument('--host', help='DB host')
    parser.add_argument('--port', help='Postgres port')
    parser.add_argument('--db', help='Database name')
    parser.add_argument('--table', help='Table name where we will store the results')
    parser.add_argument('--url', help='csv file url')
    parser.add_argument('--zones_url', help='csv file url')

    args = parser.parse_args()
    main(args)







