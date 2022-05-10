import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 1

c = C()
c.y = 2

print(c.x)
print(c.y)

print(type(c.x))
print(type(c.y))

print(isinstance(c.x, ctypes.CField))
print(isinstance(c.y, ctypes.CField))

print(isinstance(c.x, ctypes.c_int))
print(isinstance(c.y, ctypes.c_int))
</code>
Output:
<code>1
2
&lt;class 'int'&gt;
&lt;class 'int'&gt;
False
False
False
False
</code>

