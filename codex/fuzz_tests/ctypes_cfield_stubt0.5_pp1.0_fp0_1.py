import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

CField = type(C.x)

class D(object):
    pass

D.x = CField(1)

print type(D.x)
print type(C.x)
print type(S.x)
</code>
Output:
<code>&lt;type 'instancemethod'&gt;
&lt;type 'instancemethod'&gt;
&lt;type '_CField'&gt;
</code>
So the answer is: in Python 3.2, <code>type(C.x)</code> is an instance of <code>instancemethod</code>, which is a built-in type.
The <code>_CField</code> class is a bit of magic that is used by the CPython interpreter to store the field name and offset in a structure, but you can't get at it directly.

