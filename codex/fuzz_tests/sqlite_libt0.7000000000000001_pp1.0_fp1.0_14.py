import ctypes
import ctypes.util
import threading
import sqlite3 as lite
import sys
import os
import math
import glob
import datetime
import logging
import logging.handlers
import re
import yaml
import pkg_resources
import pytz
import time
import signal

import boto.ec2
import boto.ec2.elb

# We will use this to estimate the total number of rows in the database
# for the purpose of estimating the average size of a single row used
# for the calculation of the size of the database.
DEFAULT_AVERAGE_SIZE_OF_ROW_IN_DATABASE_BYTES = 200

# This is the default ulimit value. It is used if we do not get
# a value from the OS.
DEFAULT_ULIMIT_VALUE = 65536

# This is the maximum number of records that we are willing to
# commit to the database at one time. If this is set too high then
# the database may not be able to commit the data in a timely
# fashion. This can cause problems on the server in the form of
# excessive memory usage and/or excessive CPU usage.
MAX
