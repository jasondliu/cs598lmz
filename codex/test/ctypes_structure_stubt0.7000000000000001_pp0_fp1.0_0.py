import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16()
    _pack_ = True

    def _foo(self, *args):
        return self.x

class T(ctypes.Structure):
    x = ctypes.c_int16()
    _pack_ = True

    def _foo(self, *args):
        return self.x

class U(ctypes.Structure):
    x = ctypes.c_int16()
    _pack_ = True

    def _foo(self, *args):
        return self.x

class V(ctypes.Structure):
    x = ctypes.c_int16()
    _pack_ = True

    def _foo(self, *args):
        return self.x

s = S()
t = T()
u = U()
v = V()

s.x = 1
t.x = 2
u.x = 3
v.x = 4

print(s._foo() + t._foo() + u._foo() + v._foo())
