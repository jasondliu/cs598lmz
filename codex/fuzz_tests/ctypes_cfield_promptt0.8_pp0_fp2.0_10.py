import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("X", ctypes.c_int)]

o = C()
o.X = 7
print o.X

# Test ctypes.CField.from_address
a = ctypes.c_byte(ord('H'))
print type(a)
print ctypes.c_int.from_address(ctypes.addressof(a))

# Test ctypes.PyCField.from_address
import array
a = array.array('B', 'Hello World')
print ctypes.c_char.from_buffer(a)
print ctypes.c_char_p.from_buffer(a)

# Test ctypes.PyCField.from_buffer
ba = bytearray('Hello World')
print ctypes.c_short.from_buffer(ba)
print ctypes.c_short.from_buffer(ba, 1)
try:
    ctypes.c_short.from_buffer(ba, -1)
except ValueError:
    print "ValueError"

print c
