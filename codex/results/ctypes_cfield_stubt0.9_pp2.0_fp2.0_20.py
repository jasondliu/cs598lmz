import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

S.c_name = []  # Necessary for PyType_Ready to run, for some reason

class X(object):
    pass

def build_descr(name, tp, offset):
    dict = {"__name__": name,
            "__objclass__": tp,
            "offset": offset}
    return type("ctypes." + tp.__name__ + "_field", (ctypes.CField,), dict)()

for field_name, typecode in [("i", ctypes.c_int),
                             ("b", ctypes.c_byte),
                             ("c", ctypes.c_char),
                             ]:
    setattr(S, field_name, build_descr(field_name, typecode, 0))

###
print(S.i)
print(S.x)
print(bytes(S.i))
