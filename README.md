
![nyc-bike-lane-violations](https://user-images.githubusercontent.com/15967377/218378242-88826ef1-7c3d-4351-ba8e-9bdd9a79722b.png)

# bike_lane_violation
Using [sodapy](https://github.com/xmunoz/sodapy) and [Socrata Query Language](https://dev.socrata.com/docs/queries/) to get results from NYC OpenData for [Open Parking and Camera Violations](https://data.cityofnewyork.us/City-Government/Open-Parking-and-Camera-Violations/nc67-uf89) related to [Code 48](https://www.nyc.gov/site/finance/vehicles/services-violation-codes.page)
<i>`Stopping, standing or parking within a marked bicycle lane.`</i><br>
Findings will be mapped based on [Police Precinct](https://data.cityofnewyork.us/Public-Safety/Police-Precincts/78dh-3ptz)<br>

This proof of concept is utilizing 520,275 records that matched "BIKE LANE" as the violation. This of course will grow in perpetuity.
There were 476,143 that contained a unique summons number and of those we end with 473,832 that also have a valid precinct listed to do an analysis on. 

<b>Some initial questions that I have already answered:</b>

- Which boroughs and which precincts have the largest quantity of bike lane violations<br>
> As one would expect, based on where the majority of current bike lane infranstructure exists, Manhattan has the largest quantity at 270,515. 

| Borough  | QTY |
| ------------- | ------------- |
| NY   | 270515 |
| The Bronx  | 76179  |
| Brooklyn   | 65170 |
| Queens  | 43700 |
| Staten Island  | 1555|

| Precinct  | QTY |
| ------------- | ------------- |
|34     |34,412|
|33     |31,622|
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
| NY   | $32,212,198 |
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
<sub>my current solutions seem to be related to allocating funds to improve safety, commercial delivery logistics within a densely populated city and traffic reduction...<br>I have no interest in exploring reduction of bike lane blockages with an increase of policing</sub>
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

Now don't want to know?! Me too!

<img src="https://user-images.githubusercontent.com/15967377/218372588-ade79462-53bb-4f4c-88e1-c65212438589.JPG" width="250">



