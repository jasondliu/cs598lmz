import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_longlong()
    i = ctypes.c_int()

a = S()
a.x = -1.5
a.y = 2**62
a.i = 1

f = open('test.dat','wb')
f.write(a)
f.close()
#f.seek(2)
#f.write(a)
