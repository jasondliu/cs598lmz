import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.set_trace_callback
# This program depends on the python module 'matplotlib'

# Note that parameters :
#    t : The callback is called by the xTrace or sqlite3_trace() interface.
#        The value of parameter t is the same value as is passed into the xTrace
#        or sqlite3_trace() routine that causes the callback to be invoked.
#    q : The SQL statement text as UTF-8 encoded text.  Stored as a \u0000
#        terminated string.
#    p : Name of the database
#    s : Size of tmp buffer to hold hints in bytes
def trace_callback(t,q,p,s):
    print("trace_callback: t=%s q=%s p=%s s=%s" % (t,q,p,s))

if __name__ == '__main__':
    c = sqlite3.connect(':memory:')
    c.set_trace_callback(trace_callback)
    c.execute("create table test (x,y)")

    # NOTE: In Python 3.
