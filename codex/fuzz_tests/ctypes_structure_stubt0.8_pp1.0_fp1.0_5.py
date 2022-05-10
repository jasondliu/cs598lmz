import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
class V(ctypes.Structure):
    _fields_ = [('a', S * 1),
                ('b', S * 2)]
class P(ctypes.Structure):
    _anonymous_ = [('F', V)]
    _fields_ = [('G', V)]
P._pack_ = 4
print 'by value, F:', ctypes.sizeof(P, None)
print 'by value, G:', ctypes.sizeof(P, 'G')
print 'by address, F:', ctypes.sizeof(P, ctypes.addressof(P.F))
print 'by address, G:', ctypes.sizeof(P, ctypes.addressof(P.G))

# by value, F: 12
# by value, G: 12
# by address, F: 16
# by address, G: 12
