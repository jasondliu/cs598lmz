from types import FunctionType
a = (x for x in [1])
type(a)

print(type(a) is GeneratorType)
print(type(a) is not FunctionType)

print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# callable
def f():
    return 1

b = []
print(callable(f))
print(callable(b))

# file
f = open('file.txt', 'r')
print(isinstance(f, file))

# user defined class
class A:
    pass

a = A()
print(isinstance(a, A))

# builtin type
print(isinstance('s', str))
print(isinstance(1, int))
print(isinstance(1.0, float))
print(isinstance(1 + 1j, complex))
print(isinstance(True, bool))
print(isinstance([], list))
print(isinstance((), tuple))
print(isinstance({}, dict))
print(isinstance(set([1]), set))
print(isinstance([x for x in []], list))
