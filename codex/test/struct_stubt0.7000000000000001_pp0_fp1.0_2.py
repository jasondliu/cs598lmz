from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct._clearcache)

class _Struct(object):
    __slots__ = ['format', 'size']
    def __init__(self, format):
        self.format = format
        self.size = s.calcsize(format)

INT32 = _Struct('<i')
UINT32 = _Struct('<I')
INT64 = _Struct('<q')
UINT64 = _Struct('<Q')
FLOAT = _Struct('<f')
DOUBLE = _Struct('<d')

# Internal data types

class _PyTimestamp(object):
    __slots__ = ['i', 'f']
    def __init__(self, i, f):
        self.i = i
        self.f = f
    def __repr__(self):
        return '_PyTimestamp(%r, %r)' % (self.i, self.f)
    def __str__(self):
        return '%r.%r' % (self.i, self.f)


