import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#############################################################################################
# Test sqlite3.connect(":memory:")
#############################################################################################
print "Test sqlite3.connect(':memory:'):"
print "---------------------------------"
try:
    print "Create sqlite3 object without connection to database:"
    db1 = sqlite3.connect(":memory:")
    print "Type(db1) = ", type(db1)
except IOError, e:
    print "error:", e
else:
    print 'sqlite3.connect(":memory:") succeeded'
print "\n"
#############################################################################################
# Test sqlite3.connect("db1.db")
#############################################################################################
print "Test sqlite3.connect('db1.db'):"
print "---------------------------------"
try:
    print "Create sqlite3 object without connection to database:"
    db2 = sqlite3.connect("db1.db")
    print "Type(db2) = ", type(db2)
except IOError, e:
    print "error:", e
else:
    print
