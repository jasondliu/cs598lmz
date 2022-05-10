import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(12)

class Test(object):
    def __init__(self, a):
        self.value = a

    def __int__(self):
        return self.value

    def __index__(self):
        return self.value

s = S()

s.x[0] = Test(1)

a = 2

s.x[a] = 3

print s.x[a]
print s.x[0]
