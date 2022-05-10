import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test(self):
    self.x = 1

S.test = test

s = S()
print s.x
s.test()
print s.x
</code>
If you want to do this on an instance of a class, you can use <code>cls = type(self)</code>.

