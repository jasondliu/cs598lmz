import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_float
    z = ctypes.c_short

s = S()
print "sizeof(S) = %d" % (ctypes.sizeof(S),)

print 'before:', s.x, s.y, s.z

strcpy_l = ctypes.CDLL(None).strcpy
strcpy_l.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
strcpy_l.restype = ctypes.c_char_p

strcpy_l(ctypes.byref(s), "1 2 3")
print 'after:', s.x, s.y, s.z

strcpy_l(ctypes.pointer(s), "2.3 3.4 5.6")
print 'after:', s.x, s.y, s.z
