from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)

print('\n')

b = [1, 2, 3]
print(type(b))
print(type(b.__iter__))
print(type(b.__iter__) == FunctionType)

print('\n')

c = {'a': 1, 'b': 2}
print(type(c))
print(type(c.__iter__))
print(type(c.__iter__) == FunctionType)

print('\n')

d = 'abc'
print(type(d))
print(type(d.__iter__))
print(type(d.__iter__) == FunctionType)

print('\n')

e = {1, 2, 3}
print(type(e))
print(type(e.__iter__))
print(type(e.__iter__) == FunctionType)

print('\n')

f = {1: 'a', 2
