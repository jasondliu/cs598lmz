import ctypes
# Test ctypes.CField
def field_type():
    return ctypes.c_longlong

def field_input(self, object, name, value):
    object.__dict__[name] = value

def field_output(self, object, name):
    return object.__dict__[name]

class FIELD2(ctypes.CField):
    _type_ = 'q'
    _input_ = field_input
    _output_ = field_output

class X(ctypes.BigEndianStructure):
    _fields_ = [('a', FIELD2),
                ('b', FIELD2)]

# Raw
data = (ctypes.c_ubyte * 16)(0,0,0,0, 0,0,0,0, 1,0,2,0, 3,0,4,0)
copy = (ctypes.c_ubyte * 16).from_buffer(bytearray(data))
p = ctypes.c_void_p(ctypes.addressof(copy))
print(type(data), type(copy), ctypes.
