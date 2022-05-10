import types
# Test types.FunctionType
# Test types.InstanceType
# Test types.LambdaType
# Test types.MethodType
# Test types.ModuleType
# Test types.NoneType
# Test types.NotImplementedType
# Test types.TracebackType
# Test types.TypeType
# Test types.UnboundMethodType
# Test types.WrapperDescriptorType
# Test types.XRangeType

def test_types():
    import types
    # Test types.BuiltinFunctionType
    assert type(len) == types.BuiltinFunctionType
    assert type(int) == types.BuiltinFunctionType
    # Test types.BuiltinMethodType
    assert type([].append) == types.BuiltinMethodType
    assert type(().__sizeof__) == types.BuiltinMethodType
    # Test types.ClassType
    # Test types.DictProxyType
    # Test types.DictType
    assert type({}) == types.DictType
    # Test types.EllipsisType
    assert type(Ellipsis) == types.EllipsisType
    # Test types.File
