import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

X._fields_[0] = ctypes.CField(X._fields_[0])

print(X._fields_[0])
print(X._fields_[0].offset)
print(X._fields_[0].bitshift)
print(X._fields_[0].bitsize)
print(X._fields_[0].type)
print(X._fields_[0].name)

X._fields_[0] = ctypes.CField(X._fields_[0], 1, 2, 3)

print(X._fields_[0])
print(X._fields_[0].offset)
print(X._fields_[0].bitshift)
print(X._fields_[0].bitsize)
print(X._fields_[0].type)
print(X._fields_[0].name)

# Test ctypes.CField.from_address

print(ct
