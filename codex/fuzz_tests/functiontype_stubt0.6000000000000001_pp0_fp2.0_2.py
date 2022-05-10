from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.send))
print(type(a.throw))
print(type(a.close))

print(type(a.__iter__) == FunctionType)
print(type(a.__next__) == FunctionType)
print(type(a.send) == FunctionType)
print(type(a.throw) == FunctionType)
print(type(a.close) == FunctionType)
