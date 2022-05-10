import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]
</code>
(Note that there is no <code>_pack_</code> field.)
The result is a structure with a field that is not a type instance, but an int.  Now, if a structure could use one of its own fields to define its own size, you'd have a problem...
<code>class S(ctypes.Structure):
    pass
S._fields_ = [('size', ctypes.c_int),
              ('data', ctypes.c_char * S.size)]
</code>
It's impossible to implement, because you could end up in an infinite loop.

