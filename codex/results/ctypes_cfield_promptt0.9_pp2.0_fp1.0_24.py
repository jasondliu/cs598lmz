import ctypes
# Test ctypes.CField structure
    >>> class X(ctypes.Structure):
    ...     _fields_ = [('a', ctypes.c_int),
    ...                 ('b', ctypes.c_int)]
    ...     _pack_ = 1
    >>> field = ctypes.CField.from_field(X._fields_[0])
    >>> field
    CField(ba_length=32, ba_offset=0, ba_bits=0)
    >>> field.offset
    0
    >>> field.size
    4

# Test ctypes.CField structure for bit fields
    >>> class X(ctypes.Structure):
    ...     _fields_ = [('a', ctypes.c_int, 16),
    ...                 ('b', ctypes.c_int)]
    ...     _pack_ = 1
    >>> field = ctypes.CField.from_field(X._fields_[0])
    >>> field
    CField(ba_length=16, ba_offset=0, ba_bits=16)
    >>> field.offset
    0
    >>> field.size

