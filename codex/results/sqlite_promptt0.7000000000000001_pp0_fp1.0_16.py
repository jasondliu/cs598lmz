import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("dbname='%s'" % (dbname))

def set_debug(debug):
    global __DEBUG__
    __DEBUG__ = debug

def _debug(msg):
    if __DEBUG__:
        print "DEBUG: %s" % msg

__DEBUG__ = False

# inotify constants
IN_ACCESS = 0x00000001
IN_MODIFY = 0x00000002
IN_ATTRIB = 0x00000004
IN_CLOSE_WRITE = 0x00000008
IN_CLOSE_NOWRITE = 0x00000010
IN_OPEN = 0x00000020
IN_MOVED_FROM = 0x00000040
IN_MOVED_TO = 0x00000080
IN_CREATE = 0x00000100
IN_DELETE = 0x00000200
IN_DELETE_SELF = 0x00000400
IN_MOVE_SELF = 0x00000800
IN_UNMOUNT = 0x00002000
IN_Q_OVERFLOW = 0x00004000
IN_IGNORED = 0x00008000

IN_CLOSE
