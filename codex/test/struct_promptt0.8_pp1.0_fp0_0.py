import _struct
# Test _struct.Struct
# Add some extra checkings.

import _struct
import test.test_support
from test.test_support import BigEndianStructure

# Each structure used for testing like class struct_name(Structure): pass
# should be listed here to make sure it works correctly.
test_structs = []

# Helper functions

def get_size_alignment(fmt):
    fmt = _struct.__dict__[fmt].format
    size = _struct.calcsize(fmt)
    pack = _struct.pack
    pack_into = _struct.pack_into
    unpack = _struct.unpack
    unpack_from = _struct.unpack_from
    if hasattr(_struct, 'error'):
        error = _struct.error
    else:
        error = TypeError
    return fmt, size, pack, pack_into, unpack, unpack_from, error

def get_type_size(obj):
    if type(obj) == int:
        return obj
    return obj.size
