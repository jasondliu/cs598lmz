import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 10

def test_funptr():
    assert fun() == 10
    return fun

def test_funptr_call():
    f = test_funptr()
    assert f() == 10

def test_funptr_call_int():
    f = test_funptr()
    raises(TypeError, f, 1)

def test_funptr_call_kw():
    f = test_funptr()
    raises(TypeError, f, a=1)

def test_funptr_call_star():
    f = test_funptr()
    raises(TypeError, f, *[1])

def test_funptr_call_dstar():
    f = test_funptr()
    raises(TypeError, f, **{'a':1})

def test_funptr_call_star_dstar():
    f = test_funptr()
    raises(TypeError, f, *[], **{'a':1})


def test_funptr_call_int_ptr():
    f = test_funptr()
    ptr
