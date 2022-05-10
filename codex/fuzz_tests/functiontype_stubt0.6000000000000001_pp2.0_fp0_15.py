from types import FunctionType
a = (x for x in [1])
print type(a)
print isinstance(a, GeneratorType)
print isinstance(a, FunctionType)

print '-----------------------------------------'

def gen():
    yield 1
    yield 2
    yield 3

a = gen()
print type(a)
print isinstance(a, GeneratorType)
print isinstance(a, FunctionType)
