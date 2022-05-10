import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
import pprint
import requests
import sys
import re
import os

class Monitor(object):
    def __init__(self, device_id=None, database_filename=None, monitor_frequency=5, sniffs_per_sample=10,
                 show_packets=True, show_stats=False, filter_rules=None, post_url=None, post_auth=None,
                 upload_interval=120):

        # This device's unique identifier
        self.device_id = device_id

        # How frequently we should take a sample
        self.monitor_frequency = monitor_frequency

        # How frequently we should post stats to the server
        self.upload_interval = upload_interval

        # How many sniffs should we do each time we take a sample
        self.sniffs_per_sample = sniffs_per_sample

        # List of filter rules
        self.filter_rules = filter_rules

        # If set, we will post stats to this url
        self.post_url = post_url

        # If set, we
