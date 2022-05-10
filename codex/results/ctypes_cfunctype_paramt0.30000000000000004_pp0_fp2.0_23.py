import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(i):
    print "callback", i
    return i

f = FUNTYPE(callback)

#f(1)

#print f(2)

#print f(3)

#print f(4)

#print f(5)

#print f(6)

#print f(7)

#print f(8)

#print f(9)

#print f(10)

#print f(11)

#print f(12)

#print f(13)

#print f(14)

#print f(15)

#print f(16)

#print f(17)

#print f(18)

#print f(19)

#print f(20)

#print f(21)

#print f(22)

#print f(23)

#print f(24)

#print f(25)

#print f(26)

#print f(27
