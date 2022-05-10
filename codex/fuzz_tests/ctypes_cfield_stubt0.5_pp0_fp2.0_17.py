import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__str__ = lambda self: self.__name__

def print_fields(fields):
    print('\n'.join(str(field) for field in fields))

print_fields(S._fields_)
</code>
The output is:
<code>x
</code>

