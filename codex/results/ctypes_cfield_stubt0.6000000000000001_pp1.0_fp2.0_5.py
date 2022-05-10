import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    def __init__(self):
        self.x = 1

class C2(C):
    pass

o = C()

class C3(C):
    def __init__(self):
        self.x = 2

class C4(C):
    pass

class C5(C4):
    pass

class C6(C4):
    def __init__(self):
        self.x = 2

class C7(C4):
    def __init__(self):
        self.x = 2

class C8(C7):
    pass

print(type(o.x))
print(type(C.x))
print(type(C2.x))
print(type(C3.x))
print(type(C4.x))
print(type(C5.x))
print(type(C6.x))
print(type(C7.x))
print(type(C8.x))
