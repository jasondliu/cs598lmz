import ctypes
ctypes.cast(0, ctypes.py_object)

#
# The following is a hack to keep the interpreter from exiting when
# Ctrl-C is pressed.
#
import atexit
def nothing():
    pass
atexit.register(nothing)

#
# Import the low-level C++ module.
#
