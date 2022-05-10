import ctypes
import ctypes.util
import threading
import sqlite3
import csv
import sys
import signal

# init
conf_file = None
conf_db = None
process_list = []
lock = threading.Lock()

