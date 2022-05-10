import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def len_cfield(field):
    return ctypes.sizeof(field)

def array_from_pointer(field, ptr):
    return (ctypes.c_char * len_cfield(field)).from_address(ctypes.addressof(ptr.contents))

def value_from_array(field, array):
    return ctypes.cast(ctypes.pointer(array), ctypes.POINTER(field))[0]

def array_from_value(field, value):
    return (ctypes.c_char * len_cfield(field)).from_address(ctypes.addressof(value))
</code>
Using this we can write the following:
<code>p = pointer(S())
array_from_pointer(S.x, p).raw = b'\xth\xis'
print(p.contents.x)
# 220

a = array('b', [1, 2, 3])
value_from_array(S.x, a)
# c_long(12297829382473034410)
