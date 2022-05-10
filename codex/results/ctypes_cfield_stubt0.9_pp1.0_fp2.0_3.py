import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
All you need to do now is subclass <code>CField</code>:
<code>class AssignableField(ctypes.CField):
    def __init__(self, *args, **kw):
        self._assignment = kw.pop('assignment', None)
        kw['default'] = kw.get('default', None)
        setattr(self, 'assignment', self._assignment)
        super().__init__(*args, **kw)

    def _check(self, obj, val):
        if self._assignment is not None:
            val = self._assignment(val)
        super()._check(obj, val)
</code>
As it turns out, <code>ctypes</code> already supports assignment as <code>ctypes.CField.__init__</code> accepts a keyword argument <code>assignment</code>, even though it is not documented. If you pass an <code>assignment</code> function in a <code>CField</code>, it will apply that function to the input value before writing it to the structure.
