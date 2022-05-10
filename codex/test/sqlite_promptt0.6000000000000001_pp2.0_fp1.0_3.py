import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:mydatabase.db?mode=rwc', uri=True)

import time

logger = logging.getLogger(__name__)

# default config
