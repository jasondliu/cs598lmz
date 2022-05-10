import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32()
    
class C(ctypes.Structure):
    _fields_ = [('w', ctypes.c_int),
                ('s', S)]
    
s = S()
s.x = 0x11223344
    
c = C()
c.w = 0x55667788
c.s = s

