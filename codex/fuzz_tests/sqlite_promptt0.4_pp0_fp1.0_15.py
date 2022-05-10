import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('/tmp/test.db')

class Sqlite3Test(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(':memory:')

    def tearDown(self):
        self.con.close()

    def CheckError(self, exception, errtext):
        self.failUnless(isinstance(exception, sqlite3.Error))
        self.failUnlessEqual(str(exception), errtext)

    def CheckWarning(self, exception, errtext):
        self.failUnless(isinstance(exception, sqlite3.Warning))
        self.failUnlessEqual(str(exception), errtext)

    def CheckOperationalError(self, exception, errtext):
        self.failUnless(isinstance(exception, sqlite3.OperationalError))
        self.failUnlessEqual(str(exception), errtext)

    def CheckProgrammingError(self, exception, errtext):
        self.failUnless(isinstance(exception
