import ctypes
import ctypes.util
import threading
import sqlite3
import time
 
_logger = logging.getLogger('openerp.sql_db')
 
# ---------------------------------------------------------
# Low-level SQLite database interface.
# ---------------------------------------------------------
 
# Conversion between str and unicode is done through the default encoding.
# This must be set before the first convertion!
 
def db_connect(db_name):
    global connection
