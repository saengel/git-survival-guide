# This code is for the review demo

import json
import requests

def rush_hour_crashes():
    response = requests.get("https://data.cityofnewyork.us/resource/h9gi-nx95.json")

    str_response = response.content

    json_data = json.loads(str_response)

    evening_rush_count = 0
    morning_rush_count = 0

    for each in json_data:
        if '17:00' < each["crash_time"] < '20:00':
            evening_rush_count += 1
        elif'6:00' < each["crash_time"] < '9:00':
            morning_rush_count += 1

    if evening_rush_count > morning_rush_count:
        print("There are more crashes during the evening rush hour than the morning rush hour in NYC")
    else:
        print("There are more crashes during the evening rush hour than the morning rush hour in NYC")

    print(f"""
        Evening Rush Hour Crashes are {(evening_rush_count/len(json_data))*100}% of all NYC crashes \n
        Morning Rush Hour Crashes are {(morning_rush_count/len(json_data))*100}% of all NYC crashes
    """)


rush_hour_crashes()

        
