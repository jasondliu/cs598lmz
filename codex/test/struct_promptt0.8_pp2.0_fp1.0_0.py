import _struct
# Test _struct.Struct
import struct
from struct import error as StructError
import io
from test import support

from collections import namedtuple


# for more tests, see test_struct.py
# (The tests in this file are only for the _struct module, not the struct
# module.)

# _struct.Struct tests

def test_Struct_basics():
    # __new__
    assert _struct.Struct.__new__(_struct.Struct, 'f') is _struct.Struct('f')
    with support.captured_stdout() as stdout:
        _struct.Struct.__new__(_struct.Struct, 'f', verbose=True)
    assert stdout.getvalue() == 'Binary struct\n'
    # __name__
    assert _struct.Struct('f').__name__ == 'f'
    # __qualname__
    assert _struct.Struct('f').__qualname__ == 'f'
    # __doc__
