from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a,Iterable))
print(isinstance(a,Iterator))
print(isinstance(a,FunctionType))

print(isinstance(a, set))
print(isinstance(a, list))
print(isinstance(a, tuple))

b = [x for x in [1]]
print(type(b))
print(isinstance(b, list))
print(isinstance(b, tuple))
print(isinstance(b, set))
print(isinstance(b, Iterator))
print(isinstance(b, FunctionType))
