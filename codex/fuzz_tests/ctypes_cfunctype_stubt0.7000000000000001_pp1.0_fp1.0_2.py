import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
fail = fun()
"""
    py_func = cfunc_from_py_func(
        linter, "fun",
        args=tuple(),
        return_type=types.none,
        error_kind=errors.TypingError,
        flags=flags)

    assert "ctypes.py_object" in str(py_func.type)
    assert "ctypes.CFUNCTYPE(ctypes.py_object)" in str(py_func.type)
    assert "ctypes.py_object" in str(py_func.type.template)
    assert "ctypes.CFUNCTYPE(ctypes.py_object)" in str(py_func.type.template)
    assert "ctypes.py_object" in str(py_func.ctypes_function_type)


def test_ctypes_function_type_ret():
    # Define a function
    linter = test_utils.make_linter()
    flags = test_utils.MockFlags(
        no_pyobject_flags=True,
       
