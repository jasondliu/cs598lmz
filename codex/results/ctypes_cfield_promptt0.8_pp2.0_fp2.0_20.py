import ctypes
# Test ctypes.CField in C.
libc = ctypes.CDLL(None)
class foo(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

foo()
# Make sure it raises an AttributeError
try:
    foo().x = 5
except AttributeError:
    pass
else:
    fail('AttributeError not raised')
# Test CField in subclass of ctypes.Structure
class bar(ctypes.Structure):
    _fields_ = [('x', ctypes.CField),
                ('y', ctypes.c_int)]

bar()
# Make sure it raises an AttributeError
try:
    bar().x = 5
except AttributeError:
    pass
else:
    fail('AttributeError not raised')

# Test an array of CFieds
class foobar(ctypes.Structure):
    _fields_ = [('x', ctypes.CField * 4)]

foobar()
# Make sure it raises an AttributeError
try:
    foobar().x = 5
except AttributeError:
    pass
