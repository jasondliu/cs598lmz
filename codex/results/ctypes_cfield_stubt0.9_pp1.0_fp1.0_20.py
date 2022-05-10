import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
but there is no apparent way to determine the size of <code>S.x</code> and thus the total size of the structure. I don't want to use any tricks like <code>type(S.x).in_dll(S, 'x')</code>, because I want to be able to print out the offset of a field, e.g.
<code>&gt;&gt;&gt; for f in S._fields_: print(f[0], getattr(S, f[0]).offset)
...
x 0
</code>
Is there any way to do this?


A:

Here's a hacky solution:
<code>ctypes.CField = type(S.x)

def clsname(x):
    return str(type(x)).split('.')[-1]

class __cfield__(ctypes.CField):
    def __new__(cls, name, offset, scaled_size, base_type=None, shape=None):
        self = ctypes.CField.__new__(cls, name, offset
