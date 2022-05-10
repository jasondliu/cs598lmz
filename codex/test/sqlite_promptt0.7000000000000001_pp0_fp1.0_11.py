import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:', check_same_thread=False)
import sys
import argparse
import os
import matplotlib.pyplot as plt
from datetime import datetime
import time
import re
import struct
import copy
import math
import pprint
import json
import csv
import traceback

try:
    import requests
    import urllib.request as urlopen
    from urllib.error import HTTPError
    from urllib.request import urlretrieve
except ImportError:
    import urllib2 as urlopen
    from urllib2 import HTTPError
    from urllib import urlretrieve
    import StringIO
    import json

# id last updated: 15.11.2017
# https://www.reddit.com/user/spaghet/
# https://github.com/spaghet/BeatSaverDownloader/issues
# https://www.reddit.com/r/BeatSaber/comments/7wjk2g/song_download_script_2/

#MUST BE CHANGED FOR EACH NEW UPDATE
