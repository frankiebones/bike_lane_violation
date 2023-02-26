
![map_legend1](https://user-images.githubusercontent.com/15967377/221370561-8ce3b289-9868-49ef-bd25-2966295545e8.png)
<i>Map created in <a href="https://QGIS.org"><b>QGIS</b></a>  - a professional GIS application that is built on top of and proud to be itself Free and Open Source Software</i>

# bike_lane_violation

<a href="https://public.tableau.com/app/profile/frank.bucalo/viz/bike_lane_violations/Story1"><img src="https://img.shields.io/badge/Tableau-Click Here To View Tableau Story-E97627?style=flat-square&logo=Tableau&logoColor=white"></a>

Using [sodapy](https://github.com/xmunoz/sodapy) and [Socrata Query Language](https://dev.socrata.com/docs/queries/) <i>(SoQL)</i> we get records from NYC OpenData for [Open Parking and Camera Violations](https://data.cityofnewyork.us/City-Government/Open-Parking-and-Camera-Violations/nc67-uf89) related to <br><br>[Code 48](https://www.nyc.gov/site/finance/vehicles/services-violation-codes.page)
<i>`Stopping, standing or parking within a marked bicycle lane.`</i><br><br>
Records are all inserted into a [PostrgeSQL](https://www.postgresql.org/) database for futher exploratory analysis.<br><br>
Using the [Python](https://www.python.org/) library [pandas](https://pandas.pydata.org/), the records are transformed, mostly by way of removing the Summons Image column which is not necessary for our analysis as well updating some data types to properly fit our schema.<br><br>
Findings are then visualized based on [Police Precinct](https://data.cityofnewyork.us/Public-Safety/Police-Precincts/78dh-3ptz) with various python libraries such as [matplotlib](https://matplotlib.org/) and [seaborn](https://seaborn.pydata.org/) as well as geospatial libraries [geopandas](https://geopandas.org/en/stable/) and [geoplot](https://github.com/ResidentMario/geoplot). Further analysis, mapping and visualization was done with QGIS and Tableau.<br>

This proof of concept is utilizing 520,275 records that matched "BIKE LANE" as the violation. This of course will grow in perpetuity.
There were 476,143 that contained a unique summons number and of those we end with 473,832 that also have a valid precinct listed to do an analysis on. 

<b>Some initial questions that I have already answered:</b>

- Which boroughs and which precincts have the largest quantity of bike lane violations<br>
> As one would expect, based on where the majority of current bike lane infranstructure exists, Manhattan has the largest quantity at 270,515.<br>

![borough](https://user-images.githubusercontent.com/15967377/221424723-b93f57ff-47d8-49b7-984b-53d69fd138e6.JPG)

| Borough  | QTY |
| ------------- | ------------- |
| Manhattan (NY)  | 270515 |
| The Bronx (BX) | 76179  |
| Brooklyn (K)  | 65170 |
| Queens (Q) | 43700 |
| Staten Island (R)  | 1555|

The top 2 precincts are both located in the northern tip of Manhattan.<br><img src="https://user-images.githubusercontent.com/15967377/220728180-40e7c853-eb2d-49ca-8181-40da6ce77849.png" width="250"><br>
| Precinct  | QTY |
| ------------- | ------------- |
|<b>34</b>     |<b>34,412</b>|
|<b>33</b>     |<b>31,622</b>|
|9      |22,966|
|28     |19,699|
|14     |19,138|
      
- What is the total fine amount for bike lane violations per borough and precinct<br>

| Precinct  | Total Fines |
| ------------- | ------------- |
|34     |$3,846,085|
|33     |$3,505,730|
|9      |$2,519,835|
|28     |$2,195,790|
|14     |$2,140,433|

| Borough  | Total Fines |
| ------------- | ------------- |
| Manhattan    | $32,212,198 |
| The Bronx  | $8,993,183  |
| Brooklyn   | $7,666,344 |
| Queens  | $5,169,510 |
| Staten Island  | $183,105|

- Which license types are most likely to be offenders<br>
> While there are many license types listed, the majority are commercial and passenger. OMT is medallioned taxis.

| License Type  | QTY |
| ------------- | ------------- |
|COM |   237,123|
|PAS    |200,218|
| OMT     |  12,144  |

<b>Some of the questions to be answered next:</b>
- What is the total fine reduction amount given based on license type<br>
- Which license plates are the biggest repeat offenders<br>
- What is the total mileage of bike lanes in each precinct<br>
- What time of day and day of week are bike lane violations most likely to occur<br>

<b>Potential solutions to explore:</b><br>
My current solutions seem to be related to allocating funds to improve safety, ease traffic and provide realistic options to alleviate strain on commercial delivery logistics within a densely populated city...<br>
I have no interest in exploring reduction of bike lane blockages with an increase of policing.
  - Could the fines, or a portion thereof, be used to add:
    - protected bike lanes in the areas that have the most violations<br>
    - loading zones for commercial delivery in the areas/times that have the most commercial plate violations<br>
    - bike lanes (protected or not depending on the location) in commercial/manufacturing zones that are badly needed to safely connect existing cycling network<br>
    - public green space in underserved neighborhoods that are often adjacent to commercial districts<br>

<b>Additional functionality when time permits:</b>
- Airflow: weekly <i>as dataset is updated</i> API get, commit to DB, update visualizations
- Flask: web app for viewing/exploring map and data based on year, plate type & precinct

<b>The random question I wasn't looking for:</b>
- Why are there so many vehicles with Indiana passenger plates blocking bike lanes in NYC? 
  - lots of individuals skirting registration rules?
  - some sort of ride share company doing the same?

Now don't you want to know?! Me too!

<img src="https://user-images.githubusercontent.com/15967377/218372588-ade79462-53bb-4f4c-88e1-c65212438589.JPG" width="250">



