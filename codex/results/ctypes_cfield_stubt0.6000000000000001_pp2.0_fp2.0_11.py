import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def make_field(name, field_type, offset):
    return ctypes.CField(name, field_type, offset)

def make_fields(fields):
    return [make_field(*field) for field in fields]

def make_struct(name, fields):
    return type(name, (ctypes.Structure,), {'_fields_': make_fields(fields)})

S1 = make_struct('S1', (('x', ctypes.c_int, 0),))
S2 = make_struct('S2', (('x', ctypes.c_int, 0), ('y', ctypes.c_int, 4)))

print(S1())
print(S2())
</code>

