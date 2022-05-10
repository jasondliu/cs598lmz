import types
# Test types.FunctionType
assert isinstance(getattr(sys, 'getrecursionlimit'), types.FunctionType)
assert isinstance(getattr(sys, 'setrecursionlimit'), types.FunctionType)
# Test types.LambdaType
assert isinstance((lambda : None), types.LambdaType)
# Test types.GeneratorType
assert isinstance((x for x in range(5)), types.GeneratorType)
# Test types.CodeType
assert isinstance(getattr((lambda: None), '__code__'), types.CodeType)
# Test types.MappingProxyType
o = {}
assert isinstance(types.MappingProxyType(o), types.MappingProxyType)
# Test types.SimpleNamespace
assert isinstance(types.SimpleNamespace(), types.SimpleNamespace)
# Test types.MappingView
assert isinstance(types.MappingView({}), types.MappingView)
# Test types.KeysView
assert isinstance(types.KeysView({}), types.KeysView)
# Test types.ValuesView
assert isinstance(types.ValuesView({}), types.Values
