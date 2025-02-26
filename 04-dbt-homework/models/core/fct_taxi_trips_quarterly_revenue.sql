{{
    config(
        materialized='table'
    )
}}

with quarterly_revenue as (
    select 
        service_type,
        revenue_year,
        revenue_quarter,
        sum(revenue_monthly_total_amount) as quarter_revenue
    from {{ref('dm_monthly_zone_revenue')}}
    where revenue_year in (2019, 2020)
    group by 1,2,3  
)

select 
    service_type,
    revenue_year,
    revenue_quarter,
    quarter_revenue,
    LAG(quarter_revenue, 4, 1) OVER (partition by service_type order by revenue_year, revenue_quarter) as last_year_reasults,
    1.0 * (quarter_revenue - LAG(quarter_revenue, 4, 1) OVER (partition by service_type order by revenue_year, revenue_quarter)
    )/LAG(quarter_revenue, 4, 1) OVER (partition by service_type order by revenue_year, revenue_quarter) as quarterly_yoy
from quarterly_revenue
order by 1, 2, 3
