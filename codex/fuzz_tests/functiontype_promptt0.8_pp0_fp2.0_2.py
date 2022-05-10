import types
# Test types.FunctionType
# Test types.MethodType
# Test types.GeneratorType
# Test types.UnboundMethodType
# Test types.BuiltinMethodType
# Test types.ClassType
# Test types.CodeType


def test_types_getattr():
    class A:
        pass
    obj = A()
    obj.a = 2
    assert getattr(obj, 'a') == 2
    assert getattr(obj, 'b', 3) == 3
    assert getattr(obj, 'b', default=3) == 3
    #
    class B:
        def __getattribute__(self, attrname):
            if attrname == 'a':
                return 42
            else:
                raise AttributeError, attrname
    obj = B()
    assert getattr(obj, 'a') == 42
    assert getattr(obj, 'b', 3) == 3
    #
    class C:
        def __getattr__(self, attrname):
            if attrname == 'a':
                return 42
            else:
                raise AttributeError, att
