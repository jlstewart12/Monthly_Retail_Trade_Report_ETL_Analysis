## ETL, Analysis, and Visualization

ETL (extract-transform-load) is a process by which raw data is taken from a source (extract), converted and cleaned (transform), and stored into a database or data structure (load)

### Workbook and Spreadsheet layout

#### [Monthly Retail Trade Survey (MRTS) Data](https://www.census.gov/retail/index.html#mrts)

This data is often used in economics to observe and predict spending trends.

<img src="https://github.com/jlstewart12/Monthly_Retail_Trade_Report_ETL_Analysis/blob/main/src/images/static_sheet.png" height="600" width="600">

* This is a time series so each column represents sales figures recorded at a monthly interval. The headers for this dataset are highlighted in purple and will become the x-axis in line charts.
* In red, you can see that there is a tab for each year from 1992 to 2022 in descending order.
* Business categories are highlighted in blue.
* Sales figures are higlighted in green.

### Process Flow

![](https://github.com/jlstewart12/Monthly_Retail_Trade_Report_ETL_Analysis/blob/main/src/images/process_flow.png)

### Analysis & Visualization

![](https://github.com/jlstewart12/Monthly_Retail_Trade_Report_ETL_Analysis/blob/main/src/images/industry_comparisons.png)

Within this group, Sporting goods stores have the highest growth rate in sales.

### [Code](https://github.com/jlstewart12/Monthly_Retail_Trade_Report_ETL_Analysis/tree/main/src/ETL/ETL_Analysis_Visualization.ipynb)
