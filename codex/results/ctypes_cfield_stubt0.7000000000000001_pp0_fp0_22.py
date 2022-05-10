import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__str__ = lambda self: self.name

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

def dump(obj):
    if isinstance(obj, ctypes.Structure):
        items = obj.__dict__.items()
        items.sort()
    else:
        items = obj.__dict__
    for key, value in items:
        if key[0] == '_' or key in ('from_param', '_objects'):
            continue
        print '  %s:' % key,
        try:
            if isinstance(value, ctypes.Structure):
                print
                dump(value)
            elif isinstance(value, ctypes.Array):
                print '%d elements' % len(value)
            elif hasattr(value, '__dict__'):
                print
                dump(value)
            else:
                print repr(value)
        except:
            print '<ERROR>
