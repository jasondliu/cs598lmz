from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

a = [1]
print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

a = {}
print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

a = lambda x: x
print(isinstance(a, FunctionType))
print(isinstance(a, Iterable))
