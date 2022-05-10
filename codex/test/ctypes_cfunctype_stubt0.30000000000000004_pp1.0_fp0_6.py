import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_function_with_signature():
    assert call_function_with_signature(fun, [], {}) == "hello"

def test_call_function_with_signature_with_args():
    def fun(a, b, c=3, d=4):
        return a, b, c, d
    assert call_function_with_signature(fun, [1, 2], {}) == (1, 2, 3, 4)
    assert call_function_with_signature(fun, [1], {'b': 2}) == (1, 2, 3, 4)
    assert call_function_with_signature(fun, [1], {'d': 5}) == (1, 3, 3, 5)
    assert call_function_with_signature(fun, [1], {'b': 2, 'c': 6}) == (1, 2, 6, 4)
