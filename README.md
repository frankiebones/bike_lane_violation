![bike-lane-violations](https://user-images.githubusercontent.com/15967377/218348496-4ef7212b-4739-4ade-9d00-b5e691d7c11b.png)

# bike_lane_violation
Using [sodapy](https://github.com/xmunoz/sodapy) and [Socrata Query Language](https://dev.socrata.com/docs/queries/) we get results from NYC OpenData for [Open Parking and Camera Violations](https://data.cityofnewyork.us/City-Government/Open-Parking-and-Camera-Violations/nc67-uf89)<br>

We then examine all parking violation data related to [Code 48](https://www.nyc.gov/site/finance/vehicles/services-violation-codes.page)
<i>`Stopping, standing or parking within a marked bicycle lane.`</i>

This proof of concept is utilizing 512,775 records that matched "BIKE LANE" as the violation. This of course will grow in perpetuity.
There were 461,799 that contained a unique summons number and of those we end with 459,485 that also have a valid precinct listed. 


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
|34     |33,441|
|33     |30,478|
|9      |21,885|
|28     |19,094|
|14     |18,600|
      
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
| NY   | $31,124,813 |
| The Bronx  | $8,763,608  |
| Brooklyn   | $7,496,254 |
| Queens  | $5,025,780 |
| Staten Island  | $178,755|

- Which license types are most likely to be offenders<br>
> While there are many license types listed, the majority are commercial and passenger. OMT is medallioned taxis.

| License Type  | QTY |
| ------------- | ------------- |
|COM |   228818|
|PAS    |194957|
| OMT     |  11997  |




<b>Some of the questions to be answered next:</b>
- What is the total reduction amount given based on license type<br>
- Which license plates are the biggest repeat offenders<br>
- What is the total mileage of bike lanes in each precinct<br>
- What time of day and day of week are bike lane violations most likely to occur<br>

<b>Potential solutions to explore:</b><br>
<sub>my current solutions seem to be related to allocating funds to improve safety, commercial delivery logistics within a densely populated city and traffic reduction...<br>I have no interest in exploring reduction of bike lane blockages with an increase of policing</sub>
  - Could the fines, or a portion thereof, be used to add protected bike lanes in the areas that have the most violations<br>
  - Could the fines, or a portion thereof, be used to add loading zones for commercial delivery in the areas/times that have the most commercial plate violations<br>
  - Could the fines, or a portion thereof, be used to add bikes lanes (protected or not depending on the location) in commercial/manufacturing zones that are badly needed to safely connect existing cycling network infrastructure<br>

<b>Additional functionality when time permits:</b>
- Airflow: weekly <i>as dataset is updated</i> API get, commit to DB, update visualizations
- Flask: web app for viewing/exploring map and data based on year, plate type & precinct



