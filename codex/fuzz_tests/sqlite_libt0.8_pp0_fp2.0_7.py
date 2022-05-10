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
    try:
        connection = sqlite3.connect(db_name, check_same_thread=False)
        return connection
    except Exception, e:
        _logger.exception('Connecting to %s', db_name)
        raise e
 
def db_close(conn):
    global connection
    connection = None
    return conn.close()
 
def db_cursor(conn):
    try:
        return conn.cursor()
    except Exceptio
