import _struct
import _thread
import _threading
import _time
import _tkinter
import _traceback
import _types
import _warnings
import _weakref
import _webbrowser
import _winreg
import _xmlrpc
import _zipfile
import _zlib

# These are the modules that are always present in the standard library.
# If a module is not present, it is not listed here.
# This list is used to determine whether a module is frozen.
#
# Note that the 'sys' module is special: it is always frozen, but it
# is listed here, because it is a standard library module.
#
# Note that the '__main__' module is also special: it is always frozen,
# but it is not listed here, because it is not a standard library module.

_frozen_modules = {
    '_codecs', '_collections', '_functools', '_heapq', '_io', '_locale',
    '_operator', '_signal', '_sre', '_stat', '_string', '_sym
