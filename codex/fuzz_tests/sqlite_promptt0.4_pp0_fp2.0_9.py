import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/tmp/test.db")

libc = ctypes.CDLL(ctypes.util.find_library("c"))

def get_thread_id():
    return libc.syscall(186)

def get_thread_name():
    return threading.current_thread().name

def get_process_id():
    return libc.syscall(39)

def get_process_name():
    return threading.current_thread().name

def get_process_name_from_pid(pid):
    try:
        with open("/proc/%d/comm" % pid, "r") as f:
            return f.read().strip()
    except:
        return ""

def get_thread_name_from_tid(tid):
    try:
        with open("/proc/self/task/%d/comm" % tid, "r") as f:
            return f.read().strip()
    except:
        return ""

class Trace:
    def __init__(self):
        self.pid = get_process
