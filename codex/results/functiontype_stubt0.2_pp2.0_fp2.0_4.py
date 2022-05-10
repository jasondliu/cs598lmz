from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)
print(type(a) == type(print))
print(type(a) == type(lambda x: x))
print(type(a) == type(x for x in [1]))

print('\n')

b = [1, 2, 3, 4]
print(b)
print(type(b))
print(type(b) == GeneratorType)
print(type(b) == FunctionType)
print(type(b) == type(print))
print(type(b) == type(lambda x: x))
print(type(b) == type(x for x in [1]))

print('\n')

c = {'a': 1, 'b': 2}
print(c)
print(type(c))
print(type(c) == GeneratorType)
print(type(c) == FunctionType)
print(type(c) == type(print))
print(type(c) == type
