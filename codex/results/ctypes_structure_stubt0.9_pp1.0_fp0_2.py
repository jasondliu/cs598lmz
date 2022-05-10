import ctypes

class S(ctypes.Structure):
    x = ctypes.POINTER(ctypes.c_double)

class OtherStruct(ctypes.Structure):
    x = ctypes.c_char

def callback(s):
    s.test = ctypes.c_char('x')
    print s.test, ctypes.string_at(ctypes.addressof(s.test), 1)

s = ctypes.create_string_buffer('a\0', 16)
print len(s.raw), repr(s.raw)
p = ctypes.cast(ctypes.c_void_p(ctypes.addressof(s)), ctypes.POINTER(ctypes.c_char))
p[0] = 'x'

print len(s.raw), repr(s.raw)

callback(s)
print len(s.raw), repr(s.raw)

other = OtherStruct()
other.x = 'x'

print s.color, repr(s.color)
p = ctypes.cast(ctypes.c_void_p(ctypes.addressof(s)), c
