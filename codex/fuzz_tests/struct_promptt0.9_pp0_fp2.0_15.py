import _struct
# Test _struct.Struct class.
import unittest
with support.check_warnings():
    from test.support import bigmemtest
    from test.support import import_helper
    from test.support import bigaddrspacetest

# Some code taken from <mailto:jack@manyfish.co.uk> (Jack Jansen) for
# _Sys.... Get binary string representation of floating point number.

def _shorten_repr(s, l=35):
    if len(s) <= l:
        return s
    else:
        return s[:l/2-2] + '...' + s[-l/2:]

def _is_memoryview_buffer(ob):
    if not hasattr(ob, "tobytes"):
        return False
    if hasattr(ob.tobytes, "__func__"):
        return True
    if hasattr(ob.tobytes, "im_func"):
        return True
    return False

def _is_regular_buffer(ob):
    return hasattr(ob, '__array_interface__')


