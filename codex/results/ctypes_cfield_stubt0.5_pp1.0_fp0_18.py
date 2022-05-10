import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __getattribute__(self, name):
        return 42

s = S()
print s.x
s.x = C()
print s.x
s.x = "hello"
print s.x
</code>
output:
<code>0
42
42
</code>

