import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test(x):
    print x
    print ctypes.CField._length_
    print ctypes.CField._type_

def callback(x):
    print x._length_
    print x._type_
    return x

print type(callback)
print isinstance(callback, ctypes.CFuncPtr)
print isinstance(callback, type)

def callback2(x):
    print x
    print x._length_
    print x._type_
    return x

print type(callback2)
print isinstance(callback2, ctypes.CFuncPtr)
print isinstance(callback2, type)

f = ctypes.CFuncPtr(callback, ctypes.CField)
print type(f)
print isinstance(f, ctypes.CFuncPtr)
print isinstance(f, type)

test(f(S.x, 1))
test(f(S.x, None, None))
test(f(S.x, None, 2))
</code>
Runs for me on Python 2.4, 2.5
