import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

ctypes.CField.__repr__ = ctypes.CField.__str__
</code>
TypeError
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

ctypes.CField.__str__ = ctypes.CField.__repr__
</code>
NameError
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def __str__(self):
    return '{}({})'.format(self.__class__.__name__, str(type(self.type)))
ctypes.CField.__str__ = __str__

print(S.x)
</code>
<blockquote>
<p>AttributeError: 'type' object has no attribute '<strong>name</strong>'</p>
</blockquote
