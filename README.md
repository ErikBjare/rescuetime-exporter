rescuetime-exporter
===================

*Exports your RescueTime data*

**Note:** This application isn't very reliable, so far I've found no bugs but I haven't tried very hard to find them nor are there any tests so user beware. If you think something could be better, either create an issue or make the changes yourself and send in a pull request.

## Usage
Install the dependencies with `sudo python3 setup.py install`, then run the program by using `./run.sh YOUR_RESCUETIME_API_KEY`. The outfiles will be written into the `output` directory. To upload the data to Zenobase (after you've exported it from RescueTime), run `python3 to_zenobase.py`.

**WARNING:** Using the `to_zenobase.py` script can very quickly fill up your monthly Zenobase quota if you don't have a payed plan. One year was for me roughly 100000 events at the highest resolution (5min, note that one csv row is equal to one event).
The resolution can be changed manually in `rescuetime_export/main.py` however. If you have a year of RescueTime data you will be able to fit it into your monthly Zenobase quota on a free plan if you use the day resolution setting.
