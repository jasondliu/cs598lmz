import _struct
# Test _struct.Struct

def pack(fmt, *v):
    s = _struct.Struct(fmt)
    if s.size != len(s.pack(*v)):
        raise ValueError('packed %r but expected %d bytes, got %d' %
                         (v, s.size, len(s.pack(*v))))
    return s.pack(*v)

def unpack(fmt, s):
    s = _struct.Struct(fmt)
    return s.unpack(s)

def calcsize(fmt):
    return _struct.Struct(fmt).size

try:
    import array
    array_module = array
except ImportError:
    array = None
    array_module = None

try:
    import ctypes
except ImportError:
    ctypes = None

# Helper to test _struct.Struct objects for equality.
