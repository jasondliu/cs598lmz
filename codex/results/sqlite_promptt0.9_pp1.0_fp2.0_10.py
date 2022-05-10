import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(r"C:\\Users\\spsm\\pythontest.db")
# conn.cursor().execute('Execute SQL')

# For Displaying the clock in local time, you have to set time_zone in the connection
# conn = sqlite3.connect(r"C:\\Users\\spsm\\pythontest.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES, check_same_thread=False)
# conn.row_factory = sqlite3.Row
# curs = conn.cursor()
# curs.execute("select * from test")
# curs.fetchall()
# This is workinng perfectly but the rows were given as tuples, so using sqlite3.Row instead of fetching tuples all the rows are now working as dictionaries

event = threading.Event()

def get_proc_fd_usage(pid, fd):
    """
    Note: this is a UNIX-only function, raise an exception on windows since
    the structure is different
    """
