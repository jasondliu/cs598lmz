import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
</code>
This prints <code>&lt;Field type=c_int, ofs=0, size=4&gt;</code> as expected.

