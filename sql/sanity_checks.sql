-- Week 0 sanity checks: run after importing both dumps.
-- mysql -u idx_user -p idx_exchange < sql/sanity_checks.sql

-- Row counts (expect ~667k combined)
SELECT
  (SELECT COUNT(*) FROM rets_property)   AS active_listings,
  (SELECT COUNT(*) FROM california_sold) AS sold_comps;

-- Date coverage of sold data. Queries relative to CURDATE() return nothing
-- if the data ends before today, so anchor on MAX(CloseDate) instead.
SELECT MIN(CloseDate) AS first_close, MAX(CloseDate) AS last_close
FROM california_sold;

-- Listing status breakdown
SELECT L_Status, COUNT(*) AS n
FROM rets_property
GROUP BY L_Status
ORDER BY n DESC;

-- Top cities by active listings
SELECT L_City, COUNT(*) AS n
FROM rets_property
WHERE L_Status = 'Active'
GROUP BY L_City
ORDER BY n DESC
LIMIT 10;

-- How many sold rows join back to an active listing
SELECT COUNT(*) AS joined_rows
FROM california_sold cs
JOIN rets_property r ON CAST(r.L_ListingID AS UNSIGNED) = cs.ListingKey;
