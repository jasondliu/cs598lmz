import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class A(S):
    _fields_ = [('y', ctypes.c_int)]

class B(S):
    _fields_ = [('z', ctypes.c_int)]

class C(A, B):
    pass

print 'ctypes structs'
print 'x:', C.x.offset, 'y:', C.y.offset, 'z:', C.z.offset
print 'sizeof(C) =', ctypes.sizeof(C)

print 'new-style classes'
print 'x:', C.__dict__['x'].__get__.__globals__['_offset_'],
print 'y:', C.__dict__['y'].__get__.__globals__['_offset_'],
print 'z:', C.__dict__['z'].__get__.__globals__['_offset_']
print 'sizeof(C) =', C.__dict__['y'].__get__.__globals__['_size_']
