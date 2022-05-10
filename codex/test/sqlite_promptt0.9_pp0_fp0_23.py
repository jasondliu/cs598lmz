import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect to see if we are running in a 32-bit or 64-bit Python environment
# If the server is much newer than the client, the test can fail.
conn = sqlite3.connect(':memory:');
