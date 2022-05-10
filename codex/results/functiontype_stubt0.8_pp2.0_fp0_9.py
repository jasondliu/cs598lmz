from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])

def func(a, b):
    yield from a
    yield from b

def func2(a, b):
    yield from func(a, b)

assert isinstance(func(a, b), GeneratorType)
assert isinstance(func2(a, b), GeneratorType)
assert isinstance(func, FunctionType)
assert isinstance(func2, FunctionType)
assert isinstance(func2(a, b), GeneratorType)
assert list(func2(a, b)) == [1, 2]
