import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CStruct = type(S)

class C(object):
    def __init__(self, x):
        self.x = x
    def f(self):
        return self.x

def f(x):
    return x

def g(x, y):
    return x + y

def h(x):
    return x + 1

def test_call_function(space):
    w_c = space.appexec([], """():
        import ctypes
        class C(ctypes.Structure):
            _fields_ = [('x', ctypes.c_int)]
        return C(123)
    """)
    w_res = space.call_function(space.getattr(space.getattr(space.sys,
                                                           space.wrap('ctypes')),
                                              space.wrap('CFuncPtr')),
                                space.wrap(w_c.f), [], w_c)
    assert space.int_w(w_res) == 123
    w_res = space.call_function
