import _struct
# Test _struct.Struct.unpack_from
from test.support import bigaddrspacetest
from test.support import import_module
struct = import_module('struct')
import unittest
from test.support import TESTFN, unlink
MSG = b'error testing unpack'


def unpack(fmt, s):
    """
    Call struct.unpack with the given format and string,
    and check that it returns the right result.
    """
    result = _struct.unpack(fmt, s)
    expected = struct.unpack(fmt, s)
    if result != expected:
        print('%s: expected %s, got %s' %
            (fmt, (expected,), (result,)))
        print('%s: %s %s' % (fmt, repr(s), repr(result)))
        raise RuntimeError(MSG)


def unpack_from(fmt, s, offset=0):
    """
    Call struct.unpack_from with the given format, string, and offset,
    and check that it returns the right result.
    """
