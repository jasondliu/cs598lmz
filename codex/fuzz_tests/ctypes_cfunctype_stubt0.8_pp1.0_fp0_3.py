import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 3

def empty():
    pass

def test_fun_in_dict():
    d = {'a': fun}
    assert d['a']() == 3

def test_fun_in_dict2():
    d = {'a': fun, 'b': empty, 'c': empty}
    assert d['a']() == 3

def test_fun_in_dict3():
    if '__pypy__' in sys.builtin_module_names:
        py.test.skip("Unsupported on PyPy")
    d = {'a': fun, 'b': empty, 'c': empty}
    assert d['a']() == 3
    d = {'a': empty, 'b': fun, 'c': empty}
    assert d['b']() == 3
    d = {'a': empty, 'b': empty, 'c': fun}
    assert d['c']() == 3

# ____________________________________________________________

def test_noninteger_keys():
    d = {}
    d[None] = "foo"
    assert
