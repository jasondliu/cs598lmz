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

