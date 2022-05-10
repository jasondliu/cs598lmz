import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def get_func_ptr(func):
    return FUNTYPE(func)

def test_get_func_ptr():
    def func():
        pass
    ptr = get_func_ptr(func)
    assert ptr.__class__ is FUNTYPE
    assert ptr.__name__ == '<ctypes CFUNCTYPE>'
    assert ptr.__doc__ is None
    assert ptr.__module__ == '__main__'

def test_get_func_ptr_with_doc():
    def func():
        "doc"
    ptr = get_func_ptr(func)
    assert ptr.__doc__ == "doc"

def test_get_func_ptr_with_name():
    def func():
        "doc"
    ptr = get_func_ptr(func, name='name')
    assert ptr.__name__ == "name"

def test_get_func_ptr_with_module():
    def func():
        "doc"
    ptr = get_func_ptr(func, module='module')
    assert ptr.
