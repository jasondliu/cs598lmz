import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Import packages
import datetime
import os
import re
import sys
import time
import urllib.request

# Import local modules
import utilities

# Import credentials
import credentials

# Set site info
base_url = "https://www.taikai.tv/"

# Set season info
season_name = "2018/2019"
season_start_date = datetime.date(2018, 10, 1)
season_end_date = datetime.date(2019, 6, 30)

# Set tournament info
tournament_name = "World Cup"
tournament_start_date = season_start_date
tournament_end_date = season_end_date
tournament_url = base_url + "program/c/wtb_wtb_wc_2019"
tournament_full_name = "WT World Cup"
tournament_start_time = datetime.time(9, 0, 0)

# Set output paths
output_
