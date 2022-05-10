import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_char*4)]

x = X()
ctypes.c_char.from_address(ctypes.addressof(x), 4)

# Test ctypes.CFieldWithProto
class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_char*4),
                ('c', ctypes.c_char*4)]

x = X()
ctypes.c_char.from_address(ctypes.addressof(x), 4)

# Test ctypes.CFieldWithFunc
class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_char*4),
                ('c', ctypes.c_char*4),
                ('d', ctypes.c_char*4)]

x = X()
ctypes
