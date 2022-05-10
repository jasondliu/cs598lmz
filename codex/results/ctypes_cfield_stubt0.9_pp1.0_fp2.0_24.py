import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('my_int', ctypes.c_int)]

x = X()
setattr(X, 'my_int', 'hello')
print(x.my_int)
</code>
The last line prints <code>0</code> instead of raising an exception like it should. If you change the last line to <code>print(x.c_int)</code> you get a proper exception.

