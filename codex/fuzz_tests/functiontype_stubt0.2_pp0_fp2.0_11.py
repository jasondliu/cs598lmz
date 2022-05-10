from types import FunctionType
a = (x for x in [1])
b = [1]
print(type(a))
print(type(b))
print(type(b.__iter__))
print(type(b.__iter__()) == type(a))
print(type(b.__iter__) == type(a.__iter__))
print(type(b.__iter__()) == type(a.__iter__()))
print(type(b.__iter__) == type(a.__iter__))
print(type(b.__iter__) == FunctionType)
print(type(b.__iter__()) == FunctionType)
print(type(b.__iter__) == type(a.__iter__))
print(type(b.__iter__) == type(a.__iter__))
print(type(b.__iter__) == type(a.__iter__))
print(type(b.__iter__) == type(a.__iter__))
print(type(b.__iter__) == type(a.__iter__))
print(type(b.__iter__) == type(a.__
