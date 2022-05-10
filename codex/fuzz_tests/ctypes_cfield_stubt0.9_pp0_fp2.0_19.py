import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def Py_InitModule(name):
    return 1

class PyModuleDef(object):
    pass

class PyMethodDef(object):
    pass

def PyModule_Create(defs):
    return PyModuleDef()


import _ctypes

class Test_retval:
    def test_retval(self):
        _ctypes._reset_cache()
        ret = ctypes.c_int()
        assert ret.value == 0
        assert ret._objects == {}
        assert ret._b_base_ == ctypes.c_byte
        assert ret._type_ == "i"
        assert ret._length_ == 1
        if sizeof(ctypes.c_void_p) == 4:
            assert ret._sizeofinstances == 4
        else:
            assert ret._sizeofinstances == 8
        assert ret._alignment == 4
        assert ret.__doc__ == "c_long(c_int, )"


class Test_flags:
    def test_flags(self):
        _ctypes._reset_cache()
        longval
