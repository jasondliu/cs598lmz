import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() error handling.
try:
    sqlite3.connect(":memory:")
except sqlite3.Error, e:
    raise AssertionError, str(e)
# Test sqlite3.connect().cursor() error handling.
try:
    c = sqlite3.connect(":memory:")
    c.cursor()
except sqlite3.Error, e:
    raise AssertionError, str(e)
# Test sqlite3.connect().create_function() error handling.
try:
    c = sqlite3.connect(":memory:")
    c.create_function("foo")
except sqlite3.Error, e:
    raise AssertionError, str(e)
# Test sqlite3.connect().create_aggregate() error handling.
try:
    c = sqlite3.connect(":memory:")
    c.create_aggregate("foo")
except sqlite3.Error, e:
    raise AssertionError, str(e)
# Test sqlite3.connect().set_authorizer() error handling.
try:

