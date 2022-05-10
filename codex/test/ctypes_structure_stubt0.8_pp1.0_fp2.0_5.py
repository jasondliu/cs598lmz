import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    def __init__(self):
        self.x.value = 42

l = [S() for i in range(5)]

l[0].x.value = 1
for i in range(1, 5):
    l[i].x.value = l[i-1].x.value

