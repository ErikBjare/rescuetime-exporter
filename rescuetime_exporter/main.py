#!/usr/bin/python3

import os
import requests

# Settings
## Can be "month", "week", "day", "hour" or "minute"
## "minute" returns the data in 5 minute chunks, this is the highest allowed by RescueTime
resolution = "minute"

## You should probably not change this unless you really want to
script_location = os.path.dirname(os.path.realpath(__file__))
output_dir = script_location + "/../output"

def main(apikey=None, date_start=None, date_end=None):
    if not apikey:
        apikey = input("Enter your API key: ")
    if not date_start:
        date_start = input("Start date (YYYY-MM-DD): ")
    if not date_end:
        date_end = input("End date (YYYY-MM-DD): ")

    data = get_data(apikey, date_start, date_end, resolution)

    filepath = "{}/rescuetime{}-{}.csv".format(output_dir, date_start.replace("-", ""), date_end.replace("-", ""))
    with open(filepath, "w") as f:
        f.write(data)
    
    print("Output file: {}".format(filepath))
   
def get_data(apikey, date_start, date_end, resolution="hour"):
    print("Requesting data from {} to {}...".format(date_start, date_end))
    r = requests.get("http://www.rescuetime.com/anapi/data?key={}&perspective=interval&format=csv&restrict_begin={}&restrict_end={}&resolution_time={}".format(apikey, date_start, date_end, resolution))
    data = r.text

    lines = len(data.split("\n"))
    print("Received data, was {} lines long".format(len(data.split("\n"))))
    if(lines <= 1): 
        print("WARNING: If you are getting a faulty 0 or 1 line response, try a shorter time period. 3-months usually works. 1 day should absolutely work. Otherwise something is broken.")
    return data

if __name__ == "__main__":
    main()

