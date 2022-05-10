from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.__next__) == type(a.__iter__))
print(type(a.__next__) == FunctionType)
print(type(a.__iter__) == FunctionType)

print(type(a.__next__) == type(a.__iter__) == FunctionType)

print(type(a.__next__) == type(a.__iter__) == type(lambda x: x))

print(type(a.__next__) == type(a.__iter__) == type(lambda x: x) == FunctionType)

print(type(a.__next__) == type(a.__iter__) == type(lambda x: x) == type(print))

print(type(a.__next__) == type(a.__iter__) == type(lambda x: x) == type(print) == FunctionType)

print(type(a.__next__) == type(a.
