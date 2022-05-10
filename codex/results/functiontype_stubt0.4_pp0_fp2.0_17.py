from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))
print(isinstance(a, list))

for x in a:
    print(x)

print('-' * 30)

b = [x for x in [1]]
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))
print(isinstance(b, IteratorType))
print(isinstance(b, IterableType))
print(isinstance(b, list))

for x in b:
    print(x)
