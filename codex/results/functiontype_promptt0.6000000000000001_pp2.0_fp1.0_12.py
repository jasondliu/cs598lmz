import types
# Test types.FunctionType
def f(x):
    return x + 1

assert type(f) == types.FunctionType
# Test types.LambdaType
f = lambda x: x + 1

assert type(f) == types.LambdaType
# Test types.CodeType
assert type(f.__code__) == types.CodeType
# Test types.CellType
f = lambda x: x + 1
g = lambda y: x + y

assert type(f.__closure__[0]) == types.CellType
assert type(g.__closure__[0]) == types.CellType
# Test types.TypeType
assert type(int) == types.TypeType
assert type(list) == types.TypeType
assert type(dict) == types.TypeType
assert type(type) == types.TypeType
# Test types.ModuleType
assert type(types) == types.ModuleType
assert type(sys) == types.ModuleType
assert type(math) == types.ModuleType
# Test types.GeneratorType
def f():
    yield 1
    yield 2

g = f()
