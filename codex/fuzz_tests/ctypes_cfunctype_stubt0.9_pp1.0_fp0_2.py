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
class X(object):
    @pytest.mark.parametrize('x', [None])
    @FUNTYPE
    def method(self, x):
        return x is None
    """ + source)

def test_ctypes_CFUNCTYPE_dict():
    source = """
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
@FUNTYPE
def fun(x):
    d = {1: None}
    return d[x]
"""
    result = M(source)
    assert result.find("FUNTYPE")

    with pytest.raises(AssertionError):
        M(source + """
def fun(x):
    d = {None: None}
    return d[x]
""" + source
