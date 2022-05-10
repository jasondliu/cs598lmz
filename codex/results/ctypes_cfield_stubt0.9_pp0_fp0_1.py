import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)  # unbound attribute
</code>
The error is fixed by adding <code>bases=(object,)</code> to the attribute class:
<code>class CFieldType(CData, FieldType):
    def __init__(self, **kw):
        self.__dict__.update(_ctype_cache)
        super().__init__(**kw)

class CField(CData, CFieldType, bases=(object,)):
    pass

S._fields_ = [('x', CField)]
</code>

IIRC, Python 2 had a similar issue with <code>__metaclass__</code> when a metaclass didn't have a <code>__new__</code> method. It was fixed in Python 2.7, so I think it would be reasonable to apply the same fix here.

The changes here I have implemented here with a pull request. So this will work fine in the next release of ctypes, once it is merged and released.

