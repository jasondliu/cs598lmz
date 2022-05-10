import types
# Test types.FunctionType()
def test_FunctionType():
    def f(): pass
    assert type(f) is types.FunctionType

    # __name__
    assert f.__name__ == "f"

    # __code__
    assert isinstance(f.__code__, types.CodeType)
    assert f.__code__.co_argcount == 0
    assert f.__code__.co_nlocals == 0
    assert f.__code__.co_stacksize == 2
    assert f.__code__.co_flags == 67

    # __defaults__
    assert f.__defaults__ is None

    # __globals__
    assert f.__globals__ is globals()

    # __dict__
    assert f.__dict__ == {}

    # __closure__
    assert f.__closure__ is None

    # __doc__
    assert f.__doc__ is None

def test_FunctionType_with_defaults():
    def f(a=1, b=2): pass
    assert type(f) is types.FunctionType
