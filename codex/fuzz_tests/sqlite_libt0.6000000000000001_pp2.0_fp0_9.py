import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import time
import os

# This is a wrapper for the sqlite3 database to make it easier to use
# It provides a simple interface for doing a transaction which will
# rollback if an exception is raised
# It also provides a simple interface for inserting or updating data
#
# The following is a simple example of using the class:
# db = DB(db_file)
# for name, value in stuff:
#    db.write('INSERT INTO stuff VALUES (?, ?)', (name, value))
#
# db.commit()
#
# db.close()
#
# If you need to do a longer transaction, you can use the transaction
# method to automatically handle exceptions
#
# The following is an example of doing a transaction:
# db = DB(db_file)
# for name, value in stuff:
#    db.transaction(lambda: db.write('INSERT INTO stuff VALUES (?, ?)', (name, value)))
#
# db.close()
#
# You can also use the transaction method to do a transaction that
# spans multiple DB calls.  The following is
