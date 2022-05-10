import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')

# for test
#lib = ctypes.CDLL("out/myseqmodel.so")
lib = ctypes.CDLL("myseqmodel.so")

