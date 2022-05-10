import ctypes
# Test ctypes.CFUNCTYPE()

def py_f1(a,b,c):
    print(a,b,c)

f1 = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char, ctypes.c_char)(py_f1)

f1(1,2,3)

# Test ctypes.CFUNCTYPE() with a custom callback class

class Foo:

    def __init__(self):
        self.f = None

    def set_f(self, f):
        self.f = f

    def call_f(self, a, b, c):
        self.f(a, b, c)

foo = Foo()

def py_f2(a,b,c):
    print(a,b,c)

foo.set_f(ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char, ctypes.c_char)(py_f2))

foo.call_f(1,2,3)

# Test
