import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
con = sqlite3.connect(':memory:')
print("0")
# Load liblttng-ust.so
liblttng = ctypes.util.find_library('lttng-ust')
if liblttng is None:
    raise ImportError('Could not load liblttng-ust.so')
lttng_ust = ctypes.CDLL(liblttng)
print("1")
# Set up Python side tracepoint provider (name, fields)
tppython = ctypes.pythonapi.PyTrace_Provider(
    'mylib', (ctypes.c_int, ctypes.c_char_p)
)
print("2")
# Load Python-side tracepoint provider into liblttng-ust
assert 0 == lttng_ust.lttng_ust_tracepoint_register_provider(
    ctypes.pointer(tppython)
)
print("3")
# Test: Fire lttng-ust tracepoint
lttng_ust.lttng_ust_trac
