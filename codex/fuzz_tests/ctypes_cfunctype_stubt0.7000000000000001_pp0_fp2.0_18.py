import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_call_with_null_result():
    with pytest.raises(TypeError):
        fun()
