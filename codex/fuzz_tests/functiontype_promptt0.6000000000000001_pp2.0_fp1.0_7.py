import types
# Test types.FunctionType
def f():
    return 1

class C:
    def g():
        return 1

class D:
    def __init__(self):
        self.f = f
        self.g = C.g

def test():
    assert isinstance(f, types.FunctionType)
    assert isinstance(C.g, types.FunctionType)
    assert isinstance(D().f, types.FunctionType)
    assert isinstance(D().g, types.FunctionType)
    assert isinstance(D().g, types.MethodType)
    return f, C.g, D().f, D().g

def test_no_side_effect():
    # This is a regression test for a bug that was fixed, where
    # we were setting the tp_flags of classes to 0, instead of
    # or-ing with the existing flags.
    assert isinstance(str, types.ClassType)
    assert isinstance(str, type)

def test_type_is_class():
    assert isinstance(type, types.ClassType)
    assert isinstance(
