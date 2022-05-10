from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(isinstance(a.__next__, FunctionType))
print(isinstance(a.__iter__, FunctionType))

b = 'abc'
print(type(b.__iter__))
print(isinstance(b.__iter__, FunctionType))
print(isinstance(b.__next__, FunctionType))

c = list(a)
print(c)
print(type(c))
print(type(c.__iter__))
print(isinstance(c.__iter__, FunctionType))
print(isinstance(c.__next__, FunctionType))

d = iter(c)
print(type(d))
print(d)
print(type(d.__next__))
print(type(d.__iter__))
print(isinstance(d.__next__, FunctionType))
print(isinstance(d.__iter__, FunctionType))

e = next(d)
print
