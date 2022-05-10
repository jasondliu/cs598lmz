import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyStructure(ctypes.Structure):
    _fields_ = [(u'x', ctypes.c_int)]

print('MyStructure.x', type(MyStructure.x))

# MyStructure.x &lt;class 'ctypes.CField'&gt;
</code>

