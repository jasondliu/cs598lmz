import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

class C(object):
    def __init__(self):
        s = S()
        s.x = 1
        s.y = 2
        s.z = 3
        self.s = s

    def __repr__(self):
        return '&lt;C object, s.x=%d, s.y=%d, s.z=%d&gt;' % (self.s.x, self.s.y, self.s.z)

    def func(self):
        print('func called')

c = C()
c.func()
print(c)
