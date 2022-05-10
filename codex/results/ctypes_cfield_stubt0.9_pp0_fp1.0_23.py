import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, *args, **kwargs):
        for key in kwargs:
            if isinstance(kwargs[key], ctypes.CField):
                kwargs[key] = ctypes.c_int(kwargs[key].value)
        self._obj = S(*args, **kwargs)
        self._as_parameter_ = self._obj

    def __getattribute__(self, name):
        ret = object.__getattribute__(self, name)
        if isinstance(ret, ctypes.CField):
            return ret.value
        return ret

test_data = ((1, 2), (3, 4), (5, 6))
test_results = [(1, 2), (3, 4), (5, 6)]

def foo(arg):
    return arg

def bar(arg):
    return C(*arg)

@cython.test_assert_path_exists('call_unpack_complex/complex_of_complex.PyCFunction_NewEx')
@cy
