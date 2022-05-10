import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)    # obtain the CField type object
def dump(obj):
    for field in obj.__class__._fields_:
        print(field)
        print('  %r\n  ' % getattr(obj, field[0]))

s = S(-1)
print(s.x)
print(S.x.__class__)
print(dump(s))
