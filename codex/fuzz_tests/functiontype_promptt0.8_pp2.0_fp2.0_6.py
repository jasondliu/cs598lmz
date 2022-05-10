import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(tuple, types.BuiltinFunctionType)
# Test types.TypeType
assert isinstance(map, types.TypeType)
# Test types.UnboundMethodType
assert isinstance(classobj().foo, types.UnboundMethodType)
# Test types.LambdaType
assert isinstance((lambda : 1), types.LambdaType)
# Test types.GeneratorType
assert isinstance((x for x in range(3)), types.GeneratorType)

# Test types.DictProxyType
assert isinstance(type.__dict__, types.DictProxyType)

# Test types.NotImplementedType
assert isinstance(NotImplemented, types.NotImplementedType)

# Test types.GetSetDescriptorType
assert isinstance(type.__dict__.get, types.GetSetDescriptorType)

# Test types.MemberDescriptorType
assert isinstance(type.__dict__['__name__'
