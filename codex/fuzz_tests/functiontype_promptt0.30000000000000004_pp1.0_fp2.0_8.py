import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType

# Test types.LambdaType
assert type(lambda x: x) == types.LambdaType

# Test types.GeneratorType
assert type((x for x in range(10))) == types.GeneratorType

# Test types.CodeType
assert type(f.__code__) == types.CodeType

# Test types.MappingProxyType
d = {'a': 1, 'b': 2}
assert type(types.MappingProxyType(d)) == types.MappingProxyType

# Test types.SimpleNamespace
assert type(types.SimpleNamespace()) == types.SimpleNamespace

# Test types.DynamicClassAttribute
class C:
    __slots__ = ['a']
    def __init__(self):
        self.a = 1
assert type(C.a) == types.DynamicClassAttribute

# Test types.MemberDescriptorType
assert type(C.__
