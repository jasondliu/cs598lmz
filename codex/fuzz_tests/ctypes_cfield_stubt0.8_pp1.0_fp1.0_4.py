import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test():
    o = S()
    o.x = "123"
    print o.x
    '''
    Traceback (most recent call last):
      File "test.py", line 13, in <module>
        test()
      File "test.py", line 10, in test
        print o.x
    AttributeError: 'S' object has no attribute 'x'
    '''

test()
