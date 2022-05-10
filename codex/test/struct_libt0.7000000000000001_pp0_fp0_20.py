import _struct
import json
import time
import requests
import pandas as pd
import os
import datetime
import calendar

# These are the standard fields we expect in the JSON request
# If a request doesn't have one of these, it's probably not valid.
standard_fields = ("R", "H", "T", "P", "L", "A", "D", "B", "M", "G", "C", "E", "F", "Q", "O", "V")

# This is the timezone that the server is in.
# The pi/arduino is currently using Pacific time.
# If you change this, you'll have to recompile the pi/arduino code.
# TODO: add support for client-side timezone specification.
server_timezone = "America/Los_Angeles"

# These are the general parameters the user can specify when making a request:
# You can ask for data from a specific time period
# You can ask for data from a specific minute
# You can ask for data from a specific day
# You can ask for data from a specific month

# This
