import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
Python does not allow this.
I know I can subclass <code>ctypes.Structure</code> to get a type that can be used as a field, but that is not what I want. Sometimes I do not control the creation of the <code>Structure</code> subclass. When that is the case, it is inconvenient to have to create a new stub subclass just to get my field type. I want to be able to get the type directly from the field.
If possible, I want to get the field type from the field itself, not from the containing structure. That way I can use the type in other contexts.


A:

A bit late, but here's a solution (a bit hacky) from the comment posted by OP (and here too).
<code>def get_field_type(f):
    class Any(ctypes.Structure):
        _fields_ = [(f.name, type(f))]
    return Any

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

S.x_type = get_field_type
