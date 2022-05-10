import ctypes
# Test ctypes.CField

class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
    _anonymous_ = ["b"]
    _fields_ = [("b", ctypes.c_int)]

S._fields_[0]._anonymous_ = False
S._fields_[0]._name_ = "b"

S._fields_[1]._anonymous_ = False
S._fields_[1]._name_ = "a"

print S.__dict__

s = S()
print s.a
print s.b
s.a = 42
s.b = 12
print s.a
print s.b

# Test ctypes.CField.from_address
a = ctypes.c_int(42)
f = ctypes.CField.from_address(a, ctypes.c_int, "foo")
f.__set__(s, 13)
print s.a

# Test ctypes.CField.from_buffer
b = ctypes.c_buffer(1024)
f = c
