---
title: Boolean
queries:
    - long_state.sql
---

```sql state_stats
select * from handpicked.dummy
```

<DataTable data={state_stats}/>

<USMap
    data={long_state}
    state="State" 
    value="total_true_count" 
    colorScale="blue" 
    abbreviations=true
    tooltip={{
        formatter: (state) => {
            const row = long_state.find(item => item.State === state);
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