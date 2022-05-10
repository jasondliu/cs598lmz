import ctypes
import ctypes.util
import threading
import sqlite3

global_saved_core_db_file = ""
global_saved_core_db_conn = None

def read_file(filename, max_size=4096):
    with open(filename, "rb") as f:
        data = f.read(max_size)
    return data

def find_file(file_name):
    return ctypes.util.find_library(file_name)

if os.name == 'nt':
    # This should work on Windows, under both Python 2 and 3.
    def get_process_exit_code(pid):
        STILL_ACTIVE = 259
        ret = ctypes.c_long(-1)
        hproc = ctypes.windll.kernel32.OpenProcess(1, False, pid)
        ctypes.windll.kernel32.GetExitCodeProcess(hproc, ctypes.byref(ret))
        ctypes.windll.kernel32.CloseHandle(hproc)
        if ret == STILL_ACTIVE:
            return None
        return ret.value


