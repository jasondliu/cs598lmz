import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('mydata.db')
# TypeError: 'str' object is not callable test
# Test multiple threads
# https://stackoverflow.com/questions/38008079/python-sqlite3-integrityerror-attempt-to-write-a-readonly-database
# https://stackoverflow.com/questions/1894073/how-can-i-use-python-to-write-a-sqlite3-blob-to-a-file
# https://stackoverflow.com/questions/32871512/how-to-write-blob-data-to-file-with-python
#
# test
# Test the 
# Test for git
# The call to ctypes.cdll.LoadLibrary is a mac specific fix to avoid
# module not found exceptions.
# https://stackoverflow.com/questions/15174250/loading-ctypes-library-in-python-mac-osx-10-9
lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c')) 
#
#
