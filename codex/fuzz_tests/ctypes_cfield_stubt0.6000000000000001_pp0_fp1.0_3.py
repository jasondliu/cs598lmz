import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__get__(S(), None, None)
</code>
But it fails in PyPy:
<code>AttributeError: 'CField' object has no attribute '__get__'
</code>
Any idea how to fix this?


A:

I think this is a PyPy bug. It looks like the CField class is not being initialised properly. I have filed a bug report. You can work around the problem by changing your code to something like this:
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

CField = type(S.x)
CField.__get__ = CField.from_address
CField.__get__(S(), None, None)
</code>

