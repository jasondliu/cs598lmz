import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('f', ctypes.CField)]

c = C()
c.f = S.x
print(c.f)
</code>
I'm getting the error:
<code>TypeError: expected bytes, CField found
</code>
I'm using Python 3.5.2. How can I fix this?


A:

The problem is that <code>ctypes.CField</code> is not a subclass of <code>ctypes.Structure</code>, so it cannot be used as a field in a structure.
The solution is to use <code>ctypes.POINTER(ctypes.CField)</code>:
<code>class C(ctypes.Structure):
    _fields_ = [('f', ctypes.POINTER(ctypes.CField))]
</code>

