import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_double()
    def __init__(self, x, y):
        self.x = x
        self.y = y

s = S(42.42, 42.24)
print(s.x, s.y)  # 42.42 42.24
print(s)  # <__main__.S object at 0x7fcc68ad7ea8>
