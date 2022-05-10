import mmap
import os
import pickle
import re
import sys
import time
import traceback
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

from . import config
from . import db
from . import feed
from . import util
from . import web

#
# Constants
#

# The maximum number of entries to download at once.
MAX_ENTRIES = 100

# The maximum number of entries to download per feed.
MAX_FEED_ENTRIES = 20

# The maximum number of entries to download per feed per session.
MAX_FEED_SESSION_ENTRIES = 5

# The maximum number of entries to download per feed per day.
MAX_FEED_DAY_ENTRIES = 10

# The maximum number of entries to download per feed per hour.
MAX_FEED_HOUR_ENTRIES = 2

# The maximum number of entries to download per feed per minute.
MAX_FEED_MINUTE_ENTRIES = 1

# The maximum
