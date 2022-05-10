import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print 'in fun'
    return 1

#fun()

def test_call(fun):
    return fun()

print test_call(fun)

x = 1
def test_call2(fun):
    return fun()

print test_call2(lambda:x)

x = 2
print test_call2(lambda:x)
