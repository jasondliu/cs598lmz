from types import FunctionType
a = (x for x in [1])
print(type(a) == types.GeneratorType)
print(type(a) == types.GeneratorType)
print(isinstance(a, types.GeneratorType))
print(isinstance(lambda x:x, FunctionType))

b = [1,2,3]
print(isinstance(b, Iterable))
print(isinstance(b, Iterator))
c = iter(b)
print(isinstance(c, Iterable))
print(isinstance(c, Iterator))
print(list(c))
print(list(c))
print(list(c))
