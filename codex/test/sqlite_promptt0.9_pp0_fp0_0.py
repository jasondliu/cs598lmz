import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connections()

##########################################################################
#
# Wrapper using a sqlite3.Connection type
#
##########################################################################

class ConnectionWrapper(object):
    """A class which wraps sqlite3.Connection and delegates attribute
    access to it.
    """
    def __init__(self, connection):
        self.__connection = connection

    def __getattr__(self, name):
        return getattr(self.__connection, name)

##########################################################################
#
# This is a snapshot of the threading test harness used by SQLite (see the
# threadtest.c source file in the SQLite source).  We use the same basic
# test harness to test the pysqlite threading code.
#
##########################################################################

class SQLiteThread(threading.Thread):
    """A subclass of threading.Thread that runs a SQLite database
    operation in a separate thread.
    """
