from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

b = [x for x in [1]]
print(b)
print(type(b))

print(type(a.__iter__))
print(type(a.__iter__()) == a.__iter__())
print(type(a) == type(a.__iter__()))
print(id(a) == id(a.__iter__()))

c = iter(b)
print(c)
print(type(c))

print(type(b.__iter__))
print(type(b.__iter__()) == b.__iter__())
print(type(b) == type(b.__iter__()))
print(id(b) == id(b.__iter__()))

d = iter(a)
print(d)
print(type(d))

print(type(a.__iter__))
print(type(a.__iter__()) == a.__iter__())
print(type(a) == type(a.__iter__()))
print(id
