import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

s1 = S()
print s1._fields_
s1.x = 1.0
print s1.x

s2 = S()
s2.x = 2.0
print s2.x, s2.y

class B(S):
    def __iadd__(self, other):
        for i,f in enumerate(self._fields_):
            self[i] += other[i]
        return self

print B._fields_

s1.x = 1.0
s1.y = 1.0
s2.x = 2.0
s2.y = 2.0

s1 += s2
print s1.x, s1.y
