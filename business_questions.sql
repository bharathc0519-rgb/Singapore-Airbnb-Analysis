-- Q1: Region-wise average pricing
SELECT
    neighbourhood_group_cleansed AS region,
    ROUND(AVG(price), 2) AS avg_price,
    ROUND(AVG(price) - 0, 2) AS median_placeholder, -- MySQL has no native MEDIAN
    COUNT(*) AS listing_count
FROM listings
GROUP BY neighbourhood_group_cleansed
ORDER BY avg_price DESC;

-- Q2: Room-type-wise average pricing
SELECT
    room_type,
    ROUND(AVG(price), 2) AS avg_price,
    COUNT(*) AS listing_count
FROM listings
GROUP BY room_type
ORDER BY avg_price DESC;

-- Q3: Superhost impact on price & reviews
SELECT
    host_is_superhost,
    ROUND(AVG(price), 2) AS avg_price,
    ROUND(AVG(review_scores_rating), 2) AS avg_review_score,
    ROUND(AVG(number_of_reviews), 2) AS avg_num_reviews
FROM listings
GROUP BY host_is_superhost;

-- Q4: Availability distribution summary
SELECT
    MIN(availability_365) AS min_avail,
    MAX(availability_365) AS max_avail,
    ROUND(AVG(availability_365), 2) AS avg_avail,
    SUM(CASE WHEN availability_365 > 300 THEN 1 ELSE 0 END) AS low_demand_count,
    SUM(CASE WHEN availability_365 = 0 THEN 1 ELSE 0 END) AS fully_booked_count
FROM listings;

-- Q5: Top 10 most expensive neighbourhoods (min 10 listings, avoids small-sample noise)
SELECT
    neighbourhood_cleansed,
    ROUND(AVG(price), 2) AS avg_price,
    COUNT(*) AS listing_count
FROM listings
GROUP BY neighbourhood_cleansed
HAVING COUNT(*) >= 10
ORDER BY avg_price DESC
LIMIT 10;

-- Q6: Region x Room type combined pricing (pivot-style using conditional aggregation)
SELECT
    neighbourhood_group_cleansed AS region,
    ROUND(AVG(CASE WHEN room_type = 'Entire home/apt' THEN price END), 2) AS entire_home_avg,
    ROUND(AVG(CASE WHEN room_type = 'Private room' THEN price END), 2) AS private_room_avg,
    ROUND(AVG(CASE WHEN room_type = 'Shared room' THEN price END), 2) AS shared_room_avg
FROM listings
GROUP BY neighbourhood_group_cleansed
ORDER BY entire_home_avg DESC;