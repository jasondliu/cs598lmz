import ctypes
# Test ctypes.CField
cfield = ctypes.CField('foo')
# Test ctypes.CArgObject
class CAO(ctypes.CArgObject):
    _type_ = ctypes.c_int
cao = CAO()
# Test ctypes.Structure
class S(ctypes.Structure):
    _fields_ = [('foo', ctypes.c_int)]
s = S()
# Test ctypes.Array
a = (ctypes.c_int * 3)()
# Test ctypes.Union
class U(ctypes.Union):
    _fields_ = [('foo', ctypes.c_int)]
u = U()
# Test ctypes.Pointer
p = ctypes.POINTER(ctypes.c_int)()
# Test ctypes.CFuncPtr
def f1(arg):
    pass
def f2(arg):
    pass
fp1 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(f1)
fp2 = ctypes.CFUNCTYPE(ctypes.c_int, c
