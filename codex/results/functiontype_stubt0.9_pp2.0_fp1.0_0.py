from types import FunctionType
a = (x for x in [1])
b = None
c = lambda : None
d = FunctionType
print(a,b,c,d)

print(isinstance(a, GeneratorType))
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
print(isinstance(b, Iterable))
print(isinstance(c, Iterable))
print(isinstance(d, Iterable))

print(isinstance(b, Iterator))
print(isinstance(a, Callable))
print(isinstance(b, Callable))
print(isinstance(c, Callable))
print(isinstance(d, Callable))

print(issubclass(GeneratorType, Iterator))
print(issubclass(FunctionType, Callable))


# Iterable: Iterator和Generator都是Iterable
# Iterator: Generator也是Iterator，其他不是Iterator
# Generator: Generator是Iterable和Iterator
