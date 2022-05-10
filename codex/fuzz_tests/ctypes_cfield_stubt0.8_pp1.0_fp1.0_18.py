import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    pass

C._fields_ = [
    ('c', ctypes.POINTER(ctypes.CField)),
    ('d', ctypes.POINTER(0)),
    ('e', ctypes.POINTER(ctypes.c_char)),
]

print C.c
print C.d
print C.e
</code>
This was added pretty recently (in 2008), so it's probably not available in earlier versions.

