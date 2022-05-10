import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import re
from subprocess import Popen, PIPE
from time import sleep
from datetime import datetime

# Constants

# The maximum number of times to retry a failed query.
MAX_RETRIES = 5

# The number of seconds to wait between retries.
RETRY_WAIT_SECONDS = 1

# The maximum number of seconds to wait for a query to complete.
QUERY_TIMEOUT_SECONDS = 60

# The maximum number of seconds to wait for a thread to terminate.
THREAD_TIMEOUT_SECONDS = 60

# The maximum number of seconds to wait for a query to complete.
QUERY_TIMEOUT_SECONDS = 60

# The maximum number of seconds to wait for a thread to terminate.
THREAD_TIMEOUT_SECONDS = 60

# The maximum number of seconds to wait for a query to complete.
QUERY_TIMEOUT_SECONDS = 60

# The maximum number of seconds to wait for a thread to terminate.
THREAD_TIMEOUT_SECONDS = 60


