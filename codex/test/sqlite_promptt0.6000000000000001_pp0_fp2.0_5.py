import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('C:\\Users\\dwilson\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History')
# select datetime(last_visit_time/1000000-11644473600,'unixepoch'),url from urls order by last_visit_time desc limit 10;

# see https://github.com/mhammond/pywin32/blob/master/win32/Demos/taskmgr.py

def get_app_name(pid):
    """Get the name of the application for the given process ID."""
    # Open the process
    hProcess = ctypes.windll.kernel32.OpenProcess(
        PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
    if not hProcess:
        raise ctypes.WinError()
    # Get the size of the executable name
    hModule = ctypes.c_int(0)
    size = ctypes.c_uint(1024)
