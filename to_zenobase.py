import csv
import os
from datetime import datetime

from pyzenobase import ZenobaseAPI, ZenobaseEvent

# Directory where csv files from RescueTime are located
OUTPUT_DIR = "output"

BUCKET_NAME = "RescueTime Backup"

def row_to_zenobase_event(row):
    event = ZenobaseEvent({"tag": [row["Category"], row["Activity"]], 
                           "duration": int(row["Time Spent (seconds)"])*1000,
                           "timestamp": datetime.strptime(row["Date"], "%Y-%m-%dT%H:%M:%S"),
                           "rating": (int(row["Productivity"])+2)*25})
    return event


if __name__ == "__main__":
    username = input("Zenobase Username: ")
    password = input("Zenobase Password: ")
    
    with ZenobaseAPI(username, password) as zapi:
        print("Successfully authorized with Zenobase")
        bucket = zapi.create_or_get_bucket(BUCKET_NAME)
        bucket_id = bucket["@id"]
        print("Successfully created and/or found bucket '{}'".format(BUCKET_NAME))
    
        files = list(os.walk(OUTPUT_DIR))[0][2]
        files = list(filter(lambda x: ".csv" in x, files))
    
        for file in files:
            with open(OUTPUT_DIR + "/" + file) as f:
                reader = csv.DictReader(f, delimiter=",")
                events = list(map(row_to_zenobase_event, reader))
                if len(events) != 0: 
                    print("Converted {} events".format(len(events)))
                    zapi.create_events(bucket_id, events[:10])
                    print("Saved {} events to Zenobase".format(len(events)))

