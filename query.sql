SELECT 
    store,
    SUM(sales) AS total_sales
FROM sales_table
WHERE date >= '2025-01-01'
GROUP BY store
ORDER BY total_sales DESC;