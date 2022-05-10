import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'test'

def test_function_convert():
    t = dtypes.function(types.int32)
    assert t.is_function
    assert t.is_cfunction
    assert t.is_object
    assert not t.is_extension
    assert not t.is_numpy_compatible
    assert t.is_precise_type
    assert not t.is_struct
    assert not t.is_record
    assert not t.is_void_ptr
    assert not t.is_c_contiguous
    assert not t.is_f_contiguous
    assert not t.is_pointer

def test_function_convert_to_py_object():
    t = dtypes.function(types.int32)
    t2 = t.as_pyobject()
    assert t2 == dtypes.pyobject
    assert t.from_pyobject(object()) == object()
    assert t2.from_pyobject(fun) == fun

