import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.memory_used()
print 'Test connection.memory_used()'

try:
    connection = sqlite3.connect(':memory:')
    print "connection.memory_used():", connection.memory_used()
    connection.close()
except Exception, e:
    print "exception", e


# Test sqlite3.memory_used()
print 'Test sqlite3.memory_used()'

try:
    print "sqlite3.memory_used():", sqlite3.memory_used()
except Exception, e:
    print "exception", e


# Test sqlite3.threadsafe()
print 'Test sqlite3.threadsafe()'

print "sqlite3.threadsafe()", sqlite3.threadsafe()


# Test sqlite3.time()
print 'Test sqlite3.time()'

print "sqlite3.sqlite_version:", sqlite3.sqlite_version
print "sqlite3.time(execute('select 3;', None, False)):", sqlite3.time(execute, ('select 3;', None
