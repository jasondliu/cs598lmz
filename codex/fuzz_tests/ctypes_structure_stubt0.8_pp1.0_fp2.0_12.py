import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32(1)
    def __repr__(self):
        return '<S>'

p = ctypes.POINTER(S)()
print p.contents
ctypes.pointer(S()).contents = S()
print p.contents
p.contents = S()
print p.contents

class U(ctypes.Union):
    _fields_ = [('x', ctypes.c_int32)]

u = ctypes.POINTER(U)()
print u.contents
ctypes.pointer(U()).contents = U()
print u.contents
u.contents = U()
print u.contents
