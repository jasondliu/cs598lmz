import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    c = ctypes.CField(ctypes.c_int, "a+b")

x = X()
x.a = 1
x.b = 2
print(x.c)

# Test ctypes.CField with a getter and setter
class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    def getc(self):
        return self.a + self.b
    def setc(self, value):
        self.a = value - self.b
    c = ctypes.CField(ctypes.c_int, getc, setc)

y = Y()
y.a = 1
y.b = 2
print(y.c)
y.c = 3
print(y.a, y.b)

# Test ctypes.CField with a
