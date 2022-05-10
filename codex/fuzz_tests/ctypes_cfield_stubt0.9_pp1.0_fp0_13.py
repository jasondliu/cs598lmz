import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
This works, but some code relies on the presence of <code>is_qualified_type</code> and <code>FieldKind</code>, so I also need a way to convert directly to <code>Field}</code> objects, a simpler subclass of <code>Field</code> (I'm not sure this would be enough, I may need to subclass directly <code>Field</code>).
Is there an existing solution?


A:

The closest thing I can find is a factory function:
<code>def _make_cfield(name, type):
    tp = type(lambda:None)
    tp.__name__ = tp.__qualname__ = name
    return ctypes.Field(name, tp)

S._fields_ = [_make_cfield("x", ctypes.c_int)]
</code>
This actually seems to work and it's not as bad as I think it would be. If someone has a better idea, please post an answer.

