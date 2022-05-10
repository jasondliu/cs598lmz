import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#
# This test is a bit different than the other tests.  It actually
# executes the sqlite3.connect() function.  This is because we want
# to test the sqlite3.connect() function in the context of an actual
# Python process.  This is the only way to test sqlite3.connect()
# correctly because it might load the sqlite3 shared library using
# dlopen().
#
# This test is also different in that it does not use the Tcl test
# harness.  Instead, it uses the Python "unittest" module.
#
# $Id: connect.py,v 1.1 2009/01/22 02:39:07 drh Exp $

#-------------------------------------------------------------------------
# This section of code implements a class that can be used to test
# sqlite3.connect() in a subprocess.
#
# The test case "test_connect" below creates an instance of this class
# and executes the run() method in a subprocess.
#-------------------------------------------------------------------------

class ConnectTest(object):
    def __init__(self, dbname, verbose):
        self
