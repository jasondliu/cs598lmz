import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.set_trace_callback

lib = ctypes.CDLL(ctypes.util.find_library("c"))

def callback_func(sql):
    print("SQL: " + sql)
    return 0

callback_func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)
callback_func_ptr = callback_func_type(callback_func)

conn = sqlite3.connect(":memory:")
conn.set_trace_callback(callback_func_ptr)

c = conn.cursor()
c.execute("create table test(a, b)")
c.execute("insert into test(a, b) values (1, 2)")
c.execute("select * from test")

# Now switch the callback function
def callback_func2(sql):
    print("SQL2: " + sql)
    return 0

callback_func_type2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)
callback_func_ptr2
