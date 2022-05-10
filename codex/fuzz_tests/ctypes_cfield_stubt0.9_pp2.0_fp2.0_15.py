import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def make_field(name, tp, offset):
    return type(name, (ctypes.CField,),
                {"__ctype__": tp, "offset": offset})


def make_fields_from_dict(field_dict):
    if not issubclass(field_dict, ctypes.Structure):
        return make_fields_from_dict(field_dict.__dict__)
    return [make_field(name, tp, offset)
             for name, (tp, offset) in field_dict._fields_]

def total_size(fields):
    return max(f.offset + ctypes.sizeof(f.__ctype__) for f in fields)

tp = type("XPtr",
          tuple(make_fields_from_dict(
              ctypes.Structure._fields_ + [("_MyPtr", ctypes.Structure),
                          ('data', ctypes.c_void_p)]
          )) +
          (ctypes.CField,),
          {"_dynamic_": True,
           "_length_":
