import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
del S
</code>
Doing this works for Python 3.2 and 3.3, but fails for Python 3.4.  There, the <code>S.x</code> attribute appears to be an instance of <code>ctypes._CData</code> rather than <code>ctypes.Field</code>.  I get an error if I try to assign it to <code>CField</code>.
Is there a way to get the correct type in Python 3.4?


A:

The <code>_CData</code> class is a base class for all ctype instances. If you're trying to find the type of a field, you should instead look at the <code>_type_</code> attribute of the field, like so:
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x._type_)
del S
</code>

