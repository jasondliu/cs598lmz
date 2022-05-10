import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
try:
    con = sqlite3.Connection(":memory:")
except Exception:
    print("FAIL: sqlite3.Connection")
    raise SystemExit
# Test absolute linking
if ctypes.util.find_library("c") != None:
    print("PASS: ctypes.util.find_library")
else:
    print("FAIL: ctypes.util.find_library")
# Test absolute linking and static linkage
if ctypes.util.find_library("pthread") != None and ctypes.CDLL(ctypes.util.find_library("pthread")).call(threading.get_ident) == 0:
    print("PASS: ctypes.util.find_library and static linkage")
else:
    print("FAIL: ctypes.util.find_library and static linkage")
