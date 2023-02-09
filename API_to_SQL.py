import os
import requests
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from sodapy import Socrata
from config import db_password, TOKEN

client = Socrata("data.cityofnewyork.us", TOKEN, timeout=120)
url = "nc67-uf89"

# Page through the dataset.
bike_lane_df  = pd.DataFrame(columns=['plate',
                                      'state',
                                      'license_type',
                                      'summons_number',
                                      'issue_date',
                                      'violation_time',
                                      'violation',
                                      'judgment_entry_date',                                                  
                                      'fine_amount',
                                      'penalty_amount',
                                      'interest_amount',
                                      'reduction_amount',
                                      'payment_amount',
                                      'amount_due',
                                      'precinct',
                                      'county',
                                      'issuing_agency',
                                      'violation_status',
                                      'summons_image'])

for i in range(100):
    data = client.get(url, limit=1000, offset=i * 1000, where = "violation = 'BIKE LANE'")
    bike_lane_df = bike_lane_df.append(data)

bike_lane_df = bike_lane_df.drop(['summons_image'], axis=1)

db_string = f"postgresql://postgres:{db_password}@127.0.0.1:5433/bike_lane"

engine = create_engine(db_string)

bike_lane_df.to_sql(name='bike_lane', con=engine, if_exists='append', index=False)