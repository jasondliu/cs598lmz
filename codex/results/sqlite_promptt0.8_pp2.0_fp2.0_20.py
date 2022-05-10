import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect, without locking
# code is from the 3.2.2 sqlite3 python file, with the
# TRY_LOCK changed to NO_LOCK
def _verify_callable(obj):
    if not callable(obj):
        raise error, "Callback must be callable."

class _SQLiteConnection(object):
    def __init__(self, database, timeout, **kwargs):

        if not isinstance(database, unicode):
            raise error, "You must pass a unicode database name"

        self.__database_name = database

        # Check if the db can be opened before we actually open it
        # to prevent db lock issues.
        try:
            open(database, 'r').close()
        except IOError, e:
            if e.errno == 2:
                # If the file does not exist, try to create it and open it.
                fd = os.open(database, os.O_CREAT | os.O_EXCL | os.O_RDWR)
                os.close(fd)
                open(database, 'r').close()
