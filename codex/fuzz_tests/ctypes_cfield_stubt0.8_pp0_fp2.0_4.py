import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
The <code>repr()</code> of <code>ctypes.CField</code> is <code>"&lt;class 'ctypes.CField'&gt;"</code>, but I want it to be <code>"&lt;class 'ctypes.Field'&gt;"</code> in keeping with the other classes. I've tried:
<code>ctypes.CField = type(S.x)
ctypes.CField.__name__ = 'Field'
ctypes.CField.__qualname__ = 'Field'
ctypes.CField.__module__ = 'ctypes'
</code>
but that doesn't work.


A:

You cannot change the name of a class at runtime, once it has been instantiated.  The class's <code>__qualname__</code> attribute is simply a plain string, not callable.  See the docs for more.

