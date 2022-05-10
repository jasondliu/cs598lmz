import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32
    y = ctypes.c_int32
    def __str__(self):
        return "S({} {})".format(self.x, self.y)

class T(ctypes.Structure):
    x = ctypes.c_int32
    y = ctypes.c_int32
    def __str__(self):
        return "T({} {})".format(self.x, self.y)

s = S()
t = T()
s.x = 1
s.y = 1
t.x = 1
t.y = 1
print(s) # S(1 1)
print(t) # T(1 1)

#s = s + t # TypeError: unsupported operand type(s) for +: 'S' and 'T'

# https://docs.python.org/3/library/ctypes.html#ctypes.Structure.__add__
