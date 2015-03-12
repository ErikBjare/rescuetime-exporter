rescuetime-exporter
===================

*Exports your RescueTime data*

**Note:** This application isn't very reliable, so far I've found no bugs but I haven't tried very hard to find them nor are there any tests so user beware. If you think something could be better, either create an issue or make the changes yourself and send in a pull request.

## Usage
Install the dependencies with `sudo python3 setup.py install`, then run the program by using `./run.sh YOUR_RESCUETIME_API_KEY`. The outfiles will be written into the `output` directory. To upload the data to Zenobase (after you've exported it from RescueTime), run `python3 to_zenobase.py`.
