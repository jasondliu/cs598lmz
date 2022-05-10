import ctypes
ctypes.cast(0, ctypes.py_object)

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

t = Test(1, 2)
print(t.a, t.b)

t.a = 3
print(t.a, t.b)

del t.b
