{{
    config(
        materialized='table'
    )
}}

with quarterly_revenue_fare as (
    select
        service_type,
        pickup_year,
        pickup_month,
        fare_amount,
        trip_distance,
        payment_type_description
    from {{ ref('fact_trips') }}
    where fare_amount > 0 
      and trip_distance > 0 
      and payment_type_description in ('Cash', 'Credit Card')
)

select
    service_type,
    pickup_year,
    pickup_month,
    APPROX_QUANTILES(fare_amount, 100)[OFFSET(97)] as P97,
    APPROX_QUANTILES(fare_amount, 100)[OFFSET(95)] as P95,
    APPROX_QUANTILES(fare_amount, 100)[OFFSET(90)] as P90
from quarterly_revenue_fare
group by service_type, pickup_year, pickup_month
order by service_type, pickup_year, pickup_month