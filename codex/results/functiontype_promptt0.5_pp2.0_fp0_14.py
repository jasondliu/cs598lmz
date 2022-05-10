import types
# Test types.FunctionType
def test_types_functiontype():
    def f():
        pass
    assert isinstance(f, types.FunctionType)
    assert not isinstance(f, types.InstanceType)
    assert not isinstance(f, types.ClassType)
    assert not isinstance(f, types.ObjectType)
    assert not isinstance(f, types.MethodType)
    assert not isinstance(f, types.BuiltinFunctionType)
    assert not isinstance(f, types.BuiltinMethodType)
    assert not isinstance(f, types.ModuleType)
    assert not isinstance(f, types.UnboundMethodType)
    assert not isinstance(f, types.TypeType)


# Test types.InstanceType
class A:
    def f():
        pass
a = A()
assert isinstance(a, types.InstanceType)
assert not isinstance(a, types.FunctionType)
assert not isinstance(a, types.ClassType)
assert not isinstance(a, types.ObjectType)
assert not isinstance(a, types.MethodType)
assert not is
