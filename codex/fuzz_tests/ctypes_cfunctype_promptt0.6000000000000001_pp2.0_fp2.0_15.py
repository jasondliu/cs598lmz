import ctypes
# Test ctypes.CFUNCTYPE by calling a function in a shared library.

import unittest
from test import support
from ctypes import *

libc = CDLL(support.TESTFN)

# Prototype a function taking no arguments and returning an integer.
FUNC = CFUNCTYPE(c_int)

# Call the function.
libc.getpid.restype = c_int
pid = libc.getpid()

# Convert the function to a Python object.
getpid = FUNC(("getpid", libc))

# Call the Python object.
pid2 = getpid()

# This should work, too.
getpid2 = FUNC(libc.getpid)

# Check that the results are the same.
assert pid == pid2 == getpid2()

# Check that a function pointer can be called directly
assert libc.getpid() == getpid()

# Check that the repr() of a function object is meaningful
assert repr(getpid) == "<CFunctionType object at %x>" % id(getpid)

# Check that the __doc__ attribute is set
