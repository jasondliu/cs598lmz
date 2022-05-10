import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

from . import _sqlite3
from . import util
from . import _test_sqlite3

#
# Test the sqlite3 module
#

#
# Test the connection object
#

def test_threadsafety():
    # Test the value of the thread safety level.
    #
    # The thread safety level is a read-only attribute.
    #
    # The value should be an integer between 0 and 3.
    #
    # The following code tests that the value is an integer and that it is
    # within the expected range.
    #
    # The test is not exhaustive.
    #
    # The test does not test that the value is correct.
    #
    # The test does not test that the value is consistent across platforms.
    #
    # The test does not test that the value is consistent across versions.
    #
    # The test does not test that the value is consistent across builds.
    #
    # The test does not test that the value is consistent across
    # configurations.
   
