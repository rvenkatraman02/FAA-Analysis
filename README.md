# FAA-Analysis
***Analyzing Flight Delays from the Top 10 US Airlines at 10 of the Top US Airports***

**Team**: *Sarah Arnold, Marie Bennett, Sterling Hayden, Fred Lindsey, Rohan Venkatraman*

## Project Overview
Our summer practicum project analyzed flight delays within the top 10 US airlines at the top 10 US airports. With a dataset spanning from April 2022 to March 2023, we aimed to provide meaningful insights and recommendations for stakeholders, specifically targeting flight delay patterns. Our analysis was driven by the need to understand how airlines, days of the week, and times of day influence departure delays. Leveraging statistical and machine learning models, we identified key patterns and proposed recommendations to improve flight scheduling and reduce delays. This project not only showcased our analytical capabilities but also enhanced our teamwork and communication skills.

## Key Findings
Using a LASSO regression model, we determined that there were three key features that impacted **Departure Delays**:
- **Airline**: We found significant differences between the airline brand flown and departure delays. Additionally, we were able to cluster these airlines based on their characteristics.
- **Day of Week**: We found significant differences between the day of week a plane took off and its departure delay. Specifically, that Tuesday was different compared to all other days.
- **Time of Day**: We found significant differences between the time of day a plane took off and its departure delay. Additionally, there were two rush hour periods during the day, with the evening one having more delays.

## Recommendations
Based on our analysis, we recommend re-evaluating the guidance for Minimum Connection Times for certain airlines. The current rule of thumb from the IATA suggests 30-minute buffers for domestic flights. And our findings indicate that adjustments may be necessary to optimize potential passenger connections.

## Technologies Used
- Python
  - Pandas / Numpy
  - Scikit-learn
  - Scipy / Statsmodels
  - Matplotlib / Seaborn

- RStudio
 
## Data Source
The data utilized in this project is sourced from the [US DOT's Bureau of Transportation Statistics](https://transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGK&QO_fu146_anzr=b0-gvzr).

The 10 Origin Airports filtered upon: ATL, DFW, DEN, ORD, LAX, CLT, MCO, LAS, PHX, MIA

The 10 Airlines filtered upon: American, Delta, United, Southwest, Alaska, JetBlue, Spirit, Frontier, Allegiant, Hawaiian

## Data Files
`/Data_Files/` Folder containing zipped csv Master & Wrangled datasets used in our EDA and analysis.<br>
`/Data_Cleaning/` Folder containing scripts used to clean and wrangle the original DOT data.<br>
`/EDA/` Folder containing each team member's EDA to discover the business value.<br>
`Airline_Analysis.Rmd` Analysis for airline impacts on departure delay times.<br>
`Airline_Clustering_Model.ipynb` Clustering model to discover which airlines have similar behaviors.<br>
`Day_of_Week_Analysis.Rmd` Analysis for day of week impact on departure delay times.<br>
`Time_of_Day_Analysis.Rmd` Analysis for the time of day impact on departure delay times.<br>
`Investigating_Flight_Delays.pdf` Presentation given on our investigation of departure flight delays.<br>
`/Archive/` Folder containing analyses not used for our final report.
