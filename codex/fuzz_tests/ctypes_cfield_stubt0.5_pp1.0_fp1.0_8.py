import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('y', ctypes.CField)]

print(X.y)
print(X.y.__class__)
print(X.y.__class__.__bases__)
print(X.y.__class__.__bases__[0])
print(X.y.__class__.__bases__[0].__bases__)
</code>
This prints:
<code>&lt;member 'y' of 'X' objects&gt;
&lt;class '_ctypes.CField'&gt;
(&lt;class '_ctypes._CData'&gt;,)
&lt;class '_ctypes._CData'&gt;
(&lt;class 'object'&gt;,)
</code>
So, the <code>CField</code> type is a subclass of <code>_CData</code>, which is a subclass of <code>object</code>.

