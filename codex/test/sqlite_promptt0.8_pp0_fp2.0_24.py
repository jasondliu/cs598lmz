import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections
using_threaded_db_connections = True
#using_threaded_db_connections = False

if not using_threaded_db_connections:
    sqlite3.threadsafe = False

if not using_threaded_db_connections:
    print('using sqlite3 connections not designed for threads')

# 1) Connect to the database

# 1a) Using the operating system's filename character encoding
#     (so that, for example, filenames containing Chinese characters
#     on a Mac or Linux system will work).
#
#     This is the default encoding on Windows, but not on Mac or
#     Linux, and so we set it explicitly here.
#
#     Not all operating systems may support the filename
#     character encoding (for example, on Windows, 
#     sys.getfilesystemencoding() can return 'mbcs',
#     which is really code page encoding, not Unicode).
#
# If this is the case, on these operating systems, you can use
# the second method here, which specifies the encoding explicitly.

