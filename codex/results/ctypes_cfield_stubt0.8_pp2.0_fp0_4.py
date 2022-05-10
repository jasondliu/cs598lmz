import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A:
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int),
                ('w', ctypes.c_int),
                ]

a = A()
print(a.x)
print(a.y)
print(a.z)
print(a.w)

ctypes.CFuncPtr = type(ctypes.WinDLL.GetModuleHandleA)

class X(ctypes.CFuncPtr):
    _flags_ = ctypes.FUNCFLAG_CDECL

def test_function(x, y, z):
    print('x =', x)
    print('y =', y)
    print('z =', z)

X(test_function)()
