import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import argparse
import six
import pytz
import email.utils as email
import requests
import feedparser
import subprocess
import re

try:
    import pyasn
except ImportError:
    print("Please install the `pyasn` module. (www.github.com/hadiasghari/pyasn)")

# Global variables
num_threads = 2
current_time = 0
latest_new_items = []
rss_dict = {}
hostname_mutex = threading.Lock()
asnumber_mutex = threading.Lock()
dbcon_mutex = threading.Lock()
dbconn = sqlite3.connect(os.path.join('.', 'rsschaperone.db'))
c = dbconn.cursor()
