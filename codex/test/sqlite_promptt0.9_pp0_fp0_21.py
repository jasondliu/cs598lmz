import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection().connection
import _sqlite3

if os.path.exists(test.support.TESTFN):
    os.unlink(test.support.TESTFN)

# Begin test data
test.support.VS

foo_values = (
    u'bar',
    'bar',
    21,
    42.67,
    258,
    65432.34,
    35345435,
    234.2,
    234.2,
    234.2,
)
