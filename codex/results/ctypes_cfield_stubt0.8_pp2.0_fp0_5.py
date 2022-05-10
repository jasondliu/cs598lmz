import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__set__(S.x, 1)
</code>
This raises:
<code>TypeError: a float is required
</code>
Is there any way I can trick this?

There's the possibility of doing a <code>byref(pointer(int(1)))</code>, but this doesn't work because <code>ctypes.CField</code> doesn't have a <code>from_param()</code> method.

