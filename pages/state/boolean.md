---
title: Boolean
---

```sql state_stats
select * from handpicked.dummy
```

<DataTable data={state_stats}/>

```sql state_true_counts
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
```

<USMap 
    data={state_true_counts} 
    state="State" 
    value="total_true_count" 
    colorScale="blue" 
    abbreviations=true
    tooltip={{
        formatter: (state) => {
            const row = state_true_counts.find(item => item.State === state);
            return `
                <strong>${state}</strong><br>
                Total True Values: ${row.total_true_count}<br>
                ${row.passed_bills ? '✓ Has passed Bills<br>' : ''}
                ${row.legislation_bills ? '✓ Has bills in Legislation<br>' : ''}
                ${row.products_in_schools ? '✓ Products required in Schools<br>' : ''}
                ${row.products_in_buildings ? '✓ Products required in Buildings<br>' : ''}
                ${row.products_whole_state ? '✓ Products required in whole state<br>' : ''}
                ${row.products_specific_parts ? '✓ Products required in specific parts<br>' : ''}
                ${row.sales_tax_free ? '✓ Products are Sales Tax Free<br>' : ''}
            `;
        }
    }}
/>