import types
# Test types.FunctionType
def test_code_types():
    assert isinstance(lambda x: x, types.FunctionType)
    assert not isinstance(lambda x: x, types.CodeType)
    assert not isinstance(lambda x: x, types.LambdaType)
    # Test types.TracebackType
    assert isinstance(sys.last_value, types.TracebackType)
    # Test types.FrameType
    assert isinstance(sys.getframe(), types.FrameType)
    # Test types.MethodType
    class A:
        def A(self):
            pass
    a = A()
    assert isinstance(a.A, types.MethodType)


def test_type_dependency():
    import _testcapi
    assert _testcapi.get_type_dependency() == ()
    # The next line causes a TypeError to be raised.
    try:
        _testcapi.trigger_type_dependency()
    except TypeError:
        exc = sys.exc_info()[1]
        assert str(exc) == 'trigger_type_
