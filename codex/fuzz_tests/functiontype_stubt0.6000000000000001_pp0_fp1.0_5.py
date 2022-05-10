from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__iter__()) is a)

print()

b = [1]
print(type(b))
print(type(b.__iter__))
print(type(b.__iter__()) is b)

print()

c = {1}
print(type(c))
print(type(c.__iter__))
print(type(c.__iter__()) is c)

print()

d = 'abc'
print(type(d))
print(type(d.__iter__))
print(type(d.__iter__()) is d)

print()

e = {1:1}
print(type(e))
print(type(e.__iter__))
print(type(e.__iter__()) is e)

print()

f = FunctionType(lambda: None, {})
print(type(f))
print(type(f.__iter__))
print(type(f.__iter__()) is f)
