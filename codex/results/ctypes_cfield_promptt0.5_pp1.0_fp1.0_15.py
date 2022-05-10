import ctypes
# Test ctypes.CField

class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [("b", ctypes.c_int)]

def callback(f, *args):
    print "callback", f, args

# Test 1
f = ctypes.CField("a", S, T, callback)
print f.name
print f.struct_type
print f.field_type
print f.from_param
print f.to_param
print f.from_address
print f.from_buffer
print f.from_buffer_copy

# Test 2
f = ctypes.CField("a", S, None, callback)
print f.name
print f.struct_type
print f.field_type
print f.from_param
print f.to_param
print f.from_address
print f.from_buffer
print f.from_buffer_copy
