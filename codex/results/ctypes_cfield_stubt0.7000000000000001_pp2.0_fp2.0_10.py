import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def tester(cls, *args):
    print 'testing', cls, args
    o = cls(*args)
    print o.__class__
    print o
    print o[:]
    o[0] = 1
    o[1] = 2
    o[2] = 3
    o[3] = 4
    o[4] = 5
    o[5] = 6
    print o[:]
    print o[:6]
    print o[:7]
    print o[:0]
    print o[:]
    print o[1:4]
    print o[1:6]
    print o[1:7]
    print o[2:6]
    print o[2:7]
    print o[3:6]
    print o[3:7]
    print o[4:6]
    print o[4:7]
    print o[5:6]
    print o[5:7]
    print o[6:6]
    print o[6:7]
    print o[
