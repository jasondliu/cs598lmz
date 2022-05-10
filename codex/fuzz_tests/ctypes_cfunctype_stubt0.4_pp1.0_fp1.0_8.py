import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_c_fun():
    assert fun() == "hello"

def test_c_fun_pyobj():
    assert fun() == "hello"

def test_c_fun_pyobj_arg():
    assert fun() == "hello"

def test_c_fun_pyobj_arg_kw():
    assert fun() == "hello"

def test_c_fun_pyobj_arg_kw_default():
    assert fun() == "hello"

def test_c_fun_pyobj_arg_kw_default_vararg():
    assert fun() == "hello"

def test_c_fun_pyobj_arg_kw_default_vararg_kwarg():
    assert fun() == "hello"

def test_c_fun_pyobj_arg_kw_default_vararg_kwarg_annotations():
    assert fun() == "hello"

def test_c_fun_pyobj_arg_kw_default_vararg_kwarg_annotations_doc():
    assert fun() == "hello
