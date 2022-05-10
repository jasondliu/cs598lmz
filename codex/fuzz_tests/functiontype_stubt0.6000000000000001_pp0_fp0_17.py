from types import FunctionType
a = (x for x in [1])
print(type(a))

print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(dir(a))

print(hasattr(a, '__next__'))

print(a.__next__())

print(hasattr(a, '__next__'))

print(a.__next__())

print(hasattr(a, '__next__'))

print(a.__next__())

# print(a.__next__())

# print(hasattr(a, '__next__'))

print('test')
a = (x for x in [1, 2])
print(a.__next__())
print(hasattr(a, '__next__'))
print(a.__next__())
print(hasattr(a, '__next__'))
print(a.__next__())
print(hasattr(a, '__next__'))
print(a.__next__())
print(hasattr(a, '__next__'))
print(a
