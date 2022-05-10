import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("str", ctypes.CField)]
class D(ctypes.Structure):
    _fields_ = [("str", ctypes.CField)]

def test_type_error():
    import _testcapi
    raises(TypeError, _testcapi.test_type_error, 1)
    raises(TypeError, _testcapi.test_type_error, "string")
    raises(TypeError, _testcapi.test_type_error, 1.0)
    raises(TypeError, _testcapi.test_type_error, 1j)

def test_zero_length_slices():
    # Issue #1620
    import _testcapi
    _testcapi.test_zero_length_slices()

def test_with_docstring():
    def f():
        """This is a docstring"""
        pass
    assert f.__doc__ == "This is a docstring"
    #
    class A(object):
        "New-style class
