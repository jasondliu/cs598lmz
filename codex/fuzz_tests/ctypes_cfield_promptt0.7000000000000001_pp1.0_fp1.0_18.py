import ctypes
# Test ctypes.CField.from_address()

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long),
                ("z", ctypes.c_long)]

x = X()
f = ctypes.CField.from_address(ctypes.addressof(x), x._fields_[0])
print f.offset
print f.size
print f.ctype

f = ctypes.CField.from_address(ctypes.addressof(x), x._fields_[1])
print f.offset
print f.size
print f.ctype

f = ctypes.CField.from_address(ctypes.addressof(x), x._fields_[2])
print f.offset
print f.size
print f.ctype

# Test get_fields()
f = ctypes.CField.from_address(ctypes.addressof(x), x._fields_[1])
print f.get_field()

class S(ctypes.Structure):
