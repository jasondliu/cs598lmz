import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
with sqlite3.connect(":memory:") as db:
    pass

# Test sqlite3.cursor
with sqlite3.connect(":memory:") as db:
    with db.cursor() as cursor:
        pass

# Test sqlite3.connect
with sqlite3.connect(b":memory:") as db:
    pass

# Test sqlite3.cursor
with sqlite3.connect(b":memory:") as db:
    with db.cursor() as cursor:
        pass

with sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES) as db:
    pass

# Regression test of GH #1226
with sqlite3.connect(":memory:", uri=True) as db:
    with db.cursor() as cursor:
        pass

# GH #3799
with sqlite3.connect(":memory:", timeout=5.0) as db:
    with db.cursor() as cursor:
        pass

# GH #28333
