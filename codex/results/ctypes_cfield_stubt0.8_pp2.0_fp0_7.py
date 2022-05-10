import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def add_c_field(name, tp=None, ofs=None):
    if tp is not None:
        ctypes.CField.tp = tp
    if ofs is not None:
        ctypes.CField.offset = ofs
    S._fields_.append((name, ctypes.CField))

def build(name, field_list):
    return type(name, (ctypes.Structure, ), {'_fields_': field_list})

def add_c_array(name, tp, len):
    S._fields_.append((name, tp * len))

def add_c_union(name, tp):
    S._fields_.append((name, tp))

def size(s):
    return ctypes.sizeof(s)

def format_c_struct(s):
    return '%s { %s }' % (s.__name__, '; '.join(["%s: %s" % (k, v.__name__) for k, v in s._fields_]))

