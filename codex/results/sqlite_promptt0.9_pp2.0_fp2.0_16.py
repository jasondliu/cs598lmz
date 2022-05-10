import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:") for in memory database

#############################
# Version variables
#############################

# The Installation version of the eDAQ.
INSTALL_VERSION = "2.0"

class Dummy(object):

    def __init__(self, a, b, c):
        self.__dict__.update(locals())


# Add row to the database
def addrow(*args, **kwargs):
    c = kwargs.pop("cursor", None)
    db = kwargs.pop("db", None)

    if not c:
        c = db.cursor()
    
    
    insert_str = "INSERT INTO " + kwargs.pop("table", "") + " ("

    for i,elem in enumerate(args):
        if i == 0:
            # First value of iterable
            insert_str += elem
        else:
            insert_str += ", " + elem

    insert_str += ")"

    insert_str += " VALUES ("

    for i,elem in enumerate(args
