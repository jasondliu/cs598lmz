from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

print('-'*20)

b = [x for x in [1]]
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))
print(isinstance(b, Iterator))
print(isinstance(b, Iterable))

print('-'*20)

c = (x for x in [1])
print(type(c))
print(isinstance(c, GeneratorType))
print(isinstance(c, FunctionType))
print(isinstance(c, Iterator))
print(isinstance(c, Iterable))

print('-'*20)

d = [x for x in [1]]
print(type(d))
print(isinstance(d, GeneratorType))
print(isinstance(d, FunctionType))
print(isinstance(d, Iterator))
print
