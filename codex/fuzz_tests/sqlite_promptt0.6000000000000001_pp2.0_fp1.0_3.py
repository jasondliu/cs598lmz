import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:mydatabase.db?mode=rwc', uri=True)

import time

logger = logging.getLogger(__name__)

# default config
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': '',
    'charset': 'utf8mb4',
    'autocommit': True,
    'sql_mode': '',
    'time_zone': '+8:00',
    'max_connections': 5000,
    'max_cached_connections': 500,
    'max_idle_connections': 500,
    'max_recycle_sec': 30,
    'max_usage': 0,
    'connect_timeout': 10,
    'read_timeout': 10,
    'write_timeout': 10,
    'wait_timeout': 86400,
    'ping_timeout': 2,
    'pooling': True,
    'pool_name': 'MySQLPool',
   
