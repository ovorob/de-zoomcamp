{# Get quarter from date! #}

{% macro get_quarter_from_date(date) -%}

    case 
        when extract(month from {{ date }}) between 1 and 3 then 'Q1'
        when extract(month from {{ date }}) between 4 and 6 then 'Q2'
        when extract(month from {{ date }}) between 7 and 9 then 'Q3'
        when extract(month from {{ date }}) between 10 and 12 then 'Q4'
        else 'EMPTY'
    end

{%- endmacro %}