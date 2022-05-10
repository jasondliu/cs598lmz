import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object, ctypes.py_object)

def new_type():
    return type.__new__(type, 'struct', (ctypes.Structure,),
                        {'_fields_': [], 'value': ctypes.c_int})

class CTypesImplementation(object):
    def test_access(self, space):
        struct_type = new_type()
        c_int = ctypes.c_int
        struct_type._fields_ = [('a', c_int), ('b', c_int)]
        a = struct_type.from_address(61)
        a.a = -67
        assert a.a == -67
        a.b = 45
        assert a.b == 45
        assert a[1] == 45
        a[0] = -7
        assert a.a == -7
        assert a.b == 45
        raises(AttributeError, "a.c")
        raises(IndexError, "a[2]")
        raises(TypeError, "a[None]
