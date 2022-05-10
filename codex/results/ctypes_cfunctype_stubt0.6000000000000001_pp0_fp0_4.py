import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

assert fun() == 42

# This one is a bit tricky, because we need to specify that
# a function returning a function returning a function returning
# a function... returning an int, should return a function returning
# a function returning a function returning a function returning
# an int.
import sys
if sys.version_info[0] == 2:
    funtype_4_returning_int = ctypes.CFUNCTYPE(ctypes.py_object)
else:
    funtype_4_returning_int = ctypes.CFUNCTYPE(None)
    funtype_4_returning_int.return_type = ctypes.py_object
@funtype_4_returning_int
def fun():
    return fun

assert fun()()()() == fun

# The same as above, but with a function returning an int.
@funtype_4_returning_int
def fun():
    return 42

assert fun()()()() == 42

# We can also have a function returning an int returning a function returning
# an int returning a
