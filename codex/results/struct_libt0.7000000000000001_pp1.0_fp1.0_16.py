import _struct
import _heapq

#
# The module provides several useful constants and variables used by the
# standard library.
#

# The most important value is sys.version, which contains the version string
# for this interpreter.  The version_info value is a named tuple that
# contains the five components of the version number: major, minor, micro,
# releaselevel, and serial.  The version_info value corresponding to the
# Python version 2.0 is (2, 0, 0, 'final', 0).  The components can also be
# accessed by name, so sys.version_info[0] is equivalent to sys.version_info.major
# and so on.
#

version_info   = (2, 6, 0, 'final', 0)
version        = '2.6.0'
hexversion     = 0x02060000    # Version as hexadecimal number for easier
                               # interoperation with the rest of the Python
                               # ecosystem.
subversion     = ('CPython', 'tags/r261', '2063')

# platform is the platform identifier, e.
