import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def main():
    s = S()
    s.x = 3
    print(s.x)
    print(type(s.x))
    print(type(S.x))

main()
</code>
This prints:
<code>3
&lt;class 'int'&gt;
&lt;class 'ctypes.CField'&gt;
</code>
I've tried to use <code>ctypes.CField</code> as a base class for my own class, but that doesn't work:
<code>class MyField(ctypes.CField):
    pass

class S(ctypes.Structure):
    _fields_ = [('x', MyField)]

s = S()
s.x = 3
</code>
This gives the error:
<code>AttributeError: 'MyField' object has no attribute 'from_param'
</code>
So I tried to make <code>MyField</code> a subclass of <code>ctypes.c_int</code>, but that doesn't work either:
<code>class MyField
