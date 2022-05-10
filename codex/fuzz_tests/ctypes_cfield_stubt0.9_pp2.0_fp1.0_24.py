import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
Here is the error mesage I get
<blockquote>
<p>SyntaxError: cannot use starred expression here</p>
</blockquote>
I am using Python 2.7.
Thanks.


A:

You can define <code>CField</code> as a function which takes an expression, interprets it as a type, and wraps it as a <code>ctypes.Field</code>:
<code>from ctypes import Structure, c_int

class S(Structure):
    _fields_ = [('x', c_int)]

def CField(x):
    return c_int.in_dll(S(), x)
</code>
with, e.g.,
<code>print S().x == CField('x')
</code>
giving
<code>True
</code>

