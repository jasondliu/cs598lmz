from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__iter__()) == a)
print(type(a.__iter__()) == type(a))
print(type(a.__iter__()) == type(a.__iter__))
print(type(a.__iter__()) == type(a.__iter__()))
print(type(a.__iter__()) == type(a.__iter__().__iter__()))
print(type(a.__iter__()) == type(a.__iter__().__iter__().__iter__()))
print(type(a.__iter__()) == type(a.__iter__().__iter__().__iter__().__iter__()))
print(type(a.__iter__()) == type(a.__iter__().__iter__().__iter__().__iter__().__iter__()))
print(type(a.__iter__()) == type(a.__iter__().__iter__().__iter__().__iter__().__iter__().__iter__()))

