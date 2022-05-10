import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
globals()['fun'] = fun
globals()['ctypes'] = ctypes

def fun2(x):
    ''' Input: a list.
        Output: x, scrambled.'''
    x[0] = "HELLO"
    return x

