CREATE DATABASE gold_price_prediction_2026;

USE gold_price_prediction_2026;

USE gold_price_prediction_2026;

CREATE TABLE gold_daily_prices (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    price_date DATE NOT NULL,
    gold_purity SMALLINT NOT NULL,
    frequency VARCHAR(10),
    price_inr_per_10g DECIMAL(12,2),
    price_inr_per_gram DECIMAL(12,2),
    source_series VARCHAR(100),
    UNIQUE KEY unique_daily_price
    (price_date, gold_purity, source_series)
);

CREATE TABLE gold_monthly_prices (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    month_start DATE NOT NULL,
    gold_purity SMALLINT NOT NULL,
    frequency VARCHAR(10),
    price_inr_per_10g DECIMAL(12,2),
    price_inr_per_gram DECIMAL(12,2),
    source_series VARCHAR(100),
    UNIQUE KEY unique_monthly_price
    (month_start, gold_purity, source_series)
);


SELECT COUNT(*)
FROM gold_monthly_prices;


##check monthly data
select * from gold_monthly_prices
order by month_start
limit 10;

# calculate monthly average gold price
select 
	YEAR(month_start) AS year,
    MONTHNAME(month_start) AS month,
    gold_purity,
    ROUND(AVG(price_inr_per_gram),2) AS average_pricer_per_gram
from gold_monthly_prices
group by
	YEAR(month_start),
    MONTH(month_start),
    MONTHNAME(month_start),
    gold_purity
ORDER BY year, MONTH(month_start);
    
    
#Find highest and lowest gold prices
SELECT
	gold_purity,
    MAX(price_inr_per_gram) AS highest_price,
    MIN(price_inr_per_gram) AS lowest_price,
    ROUND(AVG(price_inr_per_gram),2) AS average_price
FROM gold_monthly_prices
GROUP BY gold_purity;

# Analyse 2026 gold prices
SELECT
	month_start,
    gold_purity,
    price_inr_per_gram
FROM gold_monthly_prices
WHERE month_start >='2026-01-01'
	AND month_start < '2026-11-01'
ORDER BY month_start;