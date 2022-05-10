import types
# Test types.FunctionType
def test(x):
    pass

print(type(test))
print(type(test) == types.FunctionType)
print(type(len) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.LambdaType
print(type(lambda x: x))

# Test types.GeneratorType
print(type((x for x in range(10))))

# Test types.MappingProxyType
from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
d[2] = 'B'
print(d_proxy)
print(d_proxy[2])

# Test types.SimpleNamespace
from types import SimpleNamespace
ns = SimpleNamespace()
print(ns)
ns.name = 'Hello'
print(ns)
print(ns.name)

