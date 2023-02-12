# bike_lane_violation
Using [sodapy](https://github.com/xmunoz/sodapy) and [Socrata Query Language](https://dev.socrata.com/docs/queries/) we get results from NYC OpenData for [Open Parking and Camera Violations](https://data.cityofnewyork.us/City-Government/Open-Parking-and-Camera-Violations/nc67-uf89)<br>

We then examine all parking violation data related to [Code 48](https://www.nyc.gov/site/finance/vehicles/services-violation-codes.page)
<i>`Stopping, standing or parking within a marked bicycle lane.`</i>

This proof of concept is utilizing 100,000 records at the moment.

Ultimately the plan is to put all records (from 92.6 million and counting) that and also have valid precinct, date and time information into a database then continue to get and add new data weekly via API endpoint. 

<b>Some of the questions I hope to answer now:</b>

- Which boroughs and which precincts have the largest quantity of bike lane violations<br>
- What is the total fine amount for bike lane violations per borough and precinct<br>


- Which license types are most likely to be offenders and repeat offenders<br>
- What is the total reduction amount given based on license type<br>
- Which license plates are the biggest repeat offenders<br>


<b>Some of the questions I hope to answer soon:</b>
- What is the total mileage of bike lanes in each precinct<br>
- What time of day and day of week are bike lane violations most likely to occur<br>

<b>Potential solutions to explore:</b><br>
<sub>my current solutions seem to be related to allocating funds to improve safety, commercial delivery logistics within a densely populated city and traffic reduction...<br>I have no interest in exploring reduction of bike lane blockages with an increase of policing</sub>
  - Could the fines, or a portion thereof, be used to add protected bike lanes in the areas that have the most violations<br>
  - Could the fines, or a portion thereof, be used to add loading zones for commercial delivery in the areas/times that have the most commercial plate violations<br>
  - Could the fines, or a portion thereof, be used to add bikes lanes (protected or not depending on the location) in commercial/manufacturing zones that are badly needed to safely connect existing cycling network infrastructure<br>

Visualizations
- license type breakdown
- borough breakdown
- precinct breakdown
- state plates breakdown
- base map showing precincts and heat map showing bike lane violation count

<b>Additional functionality when time permits:</b>
- Airflow: run the API get, add to DB, pull from DB, add new data to visualizations/plotting <i>(weekly as dataset is updated)</i><br>
- Flask web app for viewing/exploring map and data



