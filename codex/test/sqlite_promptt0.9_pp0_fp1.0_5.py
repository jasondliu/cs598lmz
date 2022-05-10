import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(filename, timeout)
# Add a custom timeout to the default timeout: sqlite3.connect(filename, 1.1) for a 1.1 second timeout.
# TODO: Make sure that an exception is thrown if the timeout expires.

#from libsqlite3 import db

#class timeouterror(Exception): pass

#def callfunc(func, *args):
#    if func(args) == None:
#        raise timeouterror

#def timeoutthread(waitseconds, handler, args):
#    assert waitseconds > 0
#    # wait the amount of time the function potentially is going to take,
#    # but it shouldn't take this long
#    time.sleep(waitseconds)
#    # call the functions handler
#    callfunc(handler, args)

#def sqlite3connect(timeout, *args):
#    assert timeout > 0
#    print 'connecting with timeout: %s' % timeout
#    # create a thread, which will call the functions handler
#    t = threading.Thread(target=timeoutthread, args=(timeout, handler, args))
