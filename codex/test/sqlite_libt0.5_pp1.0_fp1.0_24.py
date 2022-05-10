import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import signal
import re
import platform

from . import lib
from . import constants
from . import utils

#
# Global variables
#

# The library instance
lib = None

# The database instance
db = None

# The database lock
db_lock = threading.Lock()

# The database filename
db_filename = None

# The database connection
db_conn = None

# The database cursor
db_cursor = None

# The database schema version
db_schema_version = None

# The database schema version
db_schema_version_lock = threading.Lock()

# The database schema version
db_schema_version_changed = threading.Event()

# The database schema version
db_schema_version_changed_lock = threading.Lock()

# The database schema version
db_schema_version_changed_event = threading.Event()

# The database schema version
db_schema_version_changed_event_lock = threading.Lock()

# The
