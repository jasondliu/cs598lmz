import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
"""
    assert M(source)

    # Test error case
    with pytest.raises(AssertionError):
        assert M(source + """
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
