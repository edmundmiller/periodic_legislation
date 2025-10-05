SELECT 
    State,
    -- Calculate total TRUE values across all columns for the heatmap intensity
    SUM(CASE WHEN "Any passed Bills requiring period care" = 'TRUE' 
        OR "Any bills in Legislation requiring period care" = 'TRUE'
        OR "Period products required in Schools" = 'TRUE'
        OR "Period products required in govenement buildings" = 'TRUE'
        OR "Period products required in whole state" = 'TRUE'
        OR "Period products required in specific parts of the state" = 'TRUE'
        OR "Period products sales Tax Free" = 'TRUE' 
        THEN 1 ELSE 0 END) as total_true_count,
    -- Keep individual columns for tooltip
    SUM(CASE WHEN "Any passed Bills requiring period care" = 'TRUE' THEN 1 ELSE 0 END) AS passed_bills,
    SUM(CASE WHEN "Any bills in Legislation requiring period care" = 'TRUE' THEN 1 ELSE 0 END) AS legislation_bills,
    SUM(CASE WHEN "Period products required in Schools" = 'TRUE' THEN 1 ELSE 0 END) AS products_in_schools,
    SUM(CASE WHEN "Period products required in govenement buildings" = 'TRUE' THEN 1 ELSE 0 END) AS products_in_buildings,
    SUM(CASE WHEN "Period products required in whole state" = 'TRUE' THEN 1 ELSE 0 END) AS products_whole_state,
    SUM(CASE WHEN "Period products required in specific parts of the state" = 'TRUE' THEN 1 ELSE 0 END) AS products_specific_parts,
    SUM(CASE WHEN "Period products sales Tax Free" = 'TRUE' THEN 1 ELSE 0 END) AS sales_tax_free
FROM handpicked.dummy
GROUP BY State