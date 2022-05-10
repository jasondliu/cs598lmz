import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect with a timeout.
# This is a bit of a hack, since it doesn't actually test the timeout.
# It just makes sure that the function doesn't crash.

try:
    sqlite3.connect(":memory:", timeout=1)
except TypeError:
    pass

# Test sqlite3.connect with a timeout, when the timeout is not an int.
try:
    sqlite3.connect(":memory:", timeout="foo")
except TypeError:
    pass

# Test sqlite3.connect with a timeout, when the timeout is negative.
try:
    sqlite3.connect(":memory:", timeout=-1)
except ValueError:
    pass

# Test sqlite3.connect with a timeout, when the timeout is too large.
try:
    sqlite3.connect(":memory:", timeout=2**63)
except OverflowError:
    pass

# Test sqlite3.connect with a timeout, when the timeout is not an int,
# but is otherwise valid.
try:
    sqlite3.connect(":memory:", timeout=1.
