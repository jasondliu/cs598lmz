import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

DEFAULT = object()
def get_closure(fun, field, default=DEFAULT):
    for f in fun.__closure__ or ():
        if f.cell_contents is field:
            return f
    if default is not DEFAULT:
        return default
    raise ValueError("Can't find closure for %s" % (field,))

def test_closure_getter():
    assert get_closure(fun, default) is default
    assert get_closure(fun, default, default) is default

@jit.unroll_safe
def test_unroll_safe_closure_getter():
    n = 0
    while n < 10:
        get_closure(fun, default, default)
        n += 1


# ____________________________________________________________

def test_some_stuff():
    assert jit.isconstant(1)
    assert jit.isconstant(1.5)
    assert jit.isconstant(1.2+3.4j)
    assert jit.isconstant("foo")
    assert jit.
