import weakref
# Test weakref.ref() for objects of different tp_basicsize
# and tp_itemsize.

# Note that these tests assume that the size of a Py_ssize_t
# is the same as the size of a void*.

import sys, gc
try:
    from test import support
except ImportError:
    from test import test_support as support

# Some platforms (e.g. AIX) define Py_ssize_t as a signed type.
# In that case, this test will fail.  So we only run it if
# Py_ssize_t is an unsigned type.
if sys.maxsize > (1 << 32) and sys.maxsize > (1 << 64):
    raise support.TestSkipped('Py_ssize_t is signed (sizeof(Py_ssize_t)=%s)'
                              % (sys.maxsize.bit_length() + 1))

# Test a class with tp_basicsize and tp_itemsize

class A:
    pass

# Test a class with a small tp_basicsize and a large t
