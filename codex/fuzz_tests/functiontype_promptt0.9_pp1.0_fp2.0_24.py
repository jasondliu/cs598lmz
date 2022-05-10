import types
# Test types.FunctionType and types.MethodType

# types.ClassType won't be defined in 3.x
if types.MethodType is None:
    import test.support
    test.support.skip("need types.MethodType")

def function(self):
    """Function."""
    return self

class C:
    """Class."""

    def method(self):
        """Method."""
        return self

def test_types():
    # Test functions and methods with dummy argument
    assert type(function) is types.FunctionType
    assert type(function(None)) is types.FunctionType
    assert type(C.method) is types.MethodType
    assert type(C.method(C())) is types.MethodType
    assert type(C().method) is types.MethodType
    assert type(C().method()) is C
    # Test bound and unbound methods and descriptors
    bc = C().method
    assert type(bc) is types.MethodType
    assert type(bc) is types.MethodType
    assert type(bc) is types.MethodType
    brule = C.
