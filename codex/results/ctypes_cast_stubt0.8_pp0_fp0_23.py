import ctypes
ctypes.cast(obj, ctypes.py_object).value

# If a function needs to accept either

def decode(x, default=None):
    if isinstance(x, bytes):
        return x.decode('utf-8')
    return default


# in general, try to return a consistent type. Use None as a sentinel value to indicate special meaning.

# sometimes duck typing is the right choice to avoid extra code.
# If a function expects a sequence, use the collections.abc.Sequence abstract base class to verify that it actually is a sequence.

from collections.abc import Sequence

def is_iterable(obj):
    return isinstance(obj, Sequence)


# 8.2 Writ code to be used in multiple versions of python
from __future__ import unicode_literals


# 8.3 Know how to port Python 2 code to python 3

# the Six compatibility library

# the 2to3 source-to-source translator

# the future source-compatibility library

# 8.4 Avoid using the Python 2.x range function

# use list, xrange makes an iterator out of
