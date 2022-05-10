import ctypes
# Test ctypes.CField()

f = ctypes.Field('f', ctypes.c_long, 1, 0)
print f.offset
print ctypes.sizeof(f)

# Test ctypes.CField() with a bit field

f = ctypes.Field('f', ctypes.c_int, 2, 1)
print f.offset
print ctypes.sizeof(f)

# Test ctypes.CStruct()
# Test ctypes.sizeof()
# Test ctypes.CStruct.__slots__

class S(ctypes.CStruct):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]
    __slots__ = []
print ctypes.sizeof(S)
print S._sizeofinstances()

class S(ctypes.CStruct):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]
    __slots__ = ['a', 'b']
print ctypes.sizeof(S)
print S._size
