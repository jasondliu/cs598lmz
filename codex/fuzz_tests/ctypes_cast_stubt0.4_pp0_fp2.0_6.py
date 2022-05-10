import ctypes
ctypes.cast(0, ctypes.py_object)

# Testing that the default encoding is utf-8
# (see http://bugs.python.org/issue6580)
import sys
assert sys.getdefaultencoding() == 'utf-8'

# Testing that sys.maxint is gone, sys.maxsize should be used instead
import sys
try:
    sys.maxint
except AttributeError:
    pass
else:
    raise Exception("sys.maxint should not exist anymore")
try:
    sys.maxsize
except AttributeError:
    raise Exception("sys.maxsize should exist")

# Testing that sys.float_info is a struct sequence
import sys
assert sys.float_info.epsilon == 2.2204460492503131e-16

# Testing that sys.int_info is a struct sequence
import sys
assert sys.int_info.bits_per_digit == 30
assert sys.int_info.sizeof_digit == 4

# Testing that sys.hash_info is a struct sequence
import sys
assert sys.hash_info.width ==
