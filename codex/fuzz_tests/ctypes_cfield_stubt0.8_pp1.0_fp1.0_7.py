import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x):
        super().__init__(x)

class C(A):
    def __init__(self, x):
        super().__init__(x)

class D(S, B, C):
    pass

print(D.__mro__)
d = D(3)
print(d.x)
print(type(d.x) is ctypes.CField)
print(isinstance(d.x, ctypes.CField))
</code>
The output is:
<code>(&lt;class '__main__.D'&gt;, &lt;class '__main__.S'&gt;, &lt;class '__main__.B'&gt;, &lt;class '__main__.C'&gt;, &lt;class '__main__.A'&gt;, &lt;class 'object'&gt;)
3
True
True
