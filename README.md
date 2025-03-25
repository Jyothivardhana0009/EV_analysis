# EV_analysis


Project Workflow:
![image](https://github.com/Jyothivardhana0009/EV_analysis/blob/main/EV_workflow.png)

Data Load:
To understand the relationship between economic indicators and electric vehicle (EV) adoption, we gathered and analyzed extensive datasets:

Data.gov: Retrieved detailed economic data, including average family incomes and demographics for U.S. states.
OpenCharge: Provided comprehensive data on EV charging station distribution across states.
Zillow: Offered housing affordability and real estate market data.


Data Transformation: AWS Glue
AWS Glue handled data transformation using PySpark scripts, preparing data for analysis by:
Extracting relevant fields:
  Economic Data: state, average_family_income, population.
  EV Data: state, EV_sales, charging_station_count, timestamp.
  Housing Data: state, median_home_price, housing_affordability_index.
  Standardizing and cleaning timestamps and geographical identifiers. 
  Managing missing or inconsistent data entries.
  Storing processed data as partitioned Parquet files in Amazon S3 for efficient querying.

Data Analysis: AWS Athena
AWS Athena facilitated scalable SQL analysis to identify key relationships:
  Correlation Analysis: Investigating relationships between average family income, housing affordability, and EV adoption rates.
  Infrastructure Evaluation: Analyzing distribution and availability of EV charging stations relative to EV sales and economic indicators.
  
Data Visualization: Tableau
Visualizations were generated in Tableau to effectively communicate the analysis results:
  Income vs. EV Adoption: Illustrating the direct relationship between states’ average income and electric vehicle adoption levels.
  Charging Infrastructure Insights: Highlighting gaps and opportunities in EV charging infrastructure across different economic regions.

![image](https://github.com/Jyothivardhana0009/EV_analysis/blob/main/image.png)
![image](https://github.com/Jyothivardhana0009/EV_analysis/blob/main/EV_2.jpg)

 

 Tools & Technologies Used:
   Data Sources: Data.gov, OpenCharge, Zillow.
   AWS Lambda: Automation of data extraction. 
   Amazon S3: Secure storage of raw and processed data.
   AWS Glue: Data transformation and cataloging.
   AWS Athena: SQL-based analytics.
   Tableau: Interactive visualization and analysis presentation.
   Python, PySpark: Data processing and automation.
   JSON, CSV, Parquet: Data formats for efficient storage and retrieval.
   AWS IAM: Secure and efficient access control.

This project highlights critical economic drivers behind EV adoption and infrastructure readiness, offering valuable insights into sustainable transportation initiatives. Excited for future interdisciplinary data-driven explorations!

