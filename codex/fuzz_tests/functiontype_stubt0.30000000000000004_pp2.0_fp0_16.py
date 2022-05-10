from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.__next__) == type(a.__iter__))
print(type(a.__next__) == FunctionType)
print(type(a.__iter__) == FunctionType)
print(type(a.__next__) == type(a.__iter__) == FunctionType)
print(type(a.__next__) == type(a.__iter__) == type(a.__next__))

print(dir(a))
print(dir(a.__next__))
print(dir(a.__iter__))
print(dir(a.__next__) == dir(a.__iter__))
print(dir(a.__next__) == dir(FunctionType))
print(dir(a.__iter__) == dir(FunctionType))
print(dir(a.__next__) == dir(a.__iter__) == dir(FunctionType))
print(dir(a.__next__) == dir
