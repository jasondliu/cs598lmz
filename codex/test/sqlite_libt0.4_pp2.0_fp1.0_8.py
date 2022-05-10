import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import re
import json
import subprocess
import logging
import logging.handlers
import urllib
import urllib2

from datetime import datetime
from datetime import timedelta

from config import *

# Global variables

# The maximum number of times to retry a failed HTTP request
MAX_HTTP_RETRIES = 5

# The number of seconds to wait before retrying a failed HTTP request
HTTP_RETRY_WAIT_SECONDS = 10

# The number of seconds to wait before retrying a failed database query
DB_RETRY_WAIT_SECONDS = 10

# The number of seconds to wait before retrying a failed database query
DB_RETRY_ATTEMPTS = 5

# The number of seconds to wait before retrying a failed database query
DB_RETRY_ATTEMPTS = 5

# The number of seconds to wait before retrying a failed database query
DB_RETRY_ATTEMPTS = 5

# The number of seconds to wait before retrying a failed database query
DB_RETRY_ATTEMP
