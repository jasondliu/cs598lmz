import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/home/dri/Desktop/map.db')

try:
    if sys.path.count(os.getcwd()) < 1:
        sys.path.append(os.getcwd())
    import ossim
    import ossim_pkg_utils

except ImportError:
    print "Could not import ossim module..."
    sys.exit(1)

# Absolute path to OSIM BIN
if os.getenv('OSSIM_DEV_HOME'):
    OSSIM_INSTALL = os.getenv('OSSIM_DEV_HOME')
else:
    print >> sys.stderr, "Could not find environment variable OSSIM_DEV_HOME!"
    print >> sys.stderr, "OSSIM_DEV_HOME should be set to your OSSIM development installation's root directory."
    print >> sys.stderr, "(i.e. /home/user/ossim-dev)"
    sys.exit(1)


class Area:

    def __init__(self, x, y, w, h):
        self.x =
