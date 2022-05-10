import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test():
    s = S()
    s.x = 1
    return s

def main():
    for i in xrange(10000):
        test()

main()
