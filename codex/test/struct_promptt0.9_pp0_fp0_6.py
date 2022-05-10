import _struct
# Test _struct.Struct
from struct import calcsize

from struct import pack as _pack
from struct import unpack as _unpack

from struct import error as StructError

from test.support import import_helper

# Test equalsimple._struct.Struct
Struct = import_helper.import_module('_struct').Struct

# Helper functions

def list_equals(self, l1,l2):
    '''Check two lists have the same contents, ignoring order.'''
    l1 = list(l1)
    l2 = list(l2)
    l1.sort()
    l2.sort()
    return l1 == l2

def get_data(format):
    '''Return an appropriate data item for testing,
    given a format.'''
    if format in ('x','s','p'):
        return b''
    elif format in ('c','b','B','?'):
        return b'\x00'
    elif format in ('h','H'):
        return b'\x00\x00'
