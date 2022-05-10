import types
# Test types.FunctionType
def foo(x, y):
    return x + y

type(foo) == types.FunctionType

# Test types.LambdaType
foo2 = lambda x, y: x + y

type(foo2) == types.LambdaType

# Test types.GeneratorType
def foo3():
    for i in range(10):
        yield i

type(foo3()) == types.GeneratorType

# Test types.MappingProxyType
d = {'foo': 'bar'}
d2 = types.MappingProxyType(d)

d2['foo'] == 'bar'
d2['other'] = 'other'

# Test types.SimpleNamespace
ns = types.SimpleNamespace()
ns.foo = 'bar'
ns.foo == 'bar'

# Test types.ModuleType
m = types.ModuleType('test')
m.foo = 'bar'

m.foo == 'bar'
