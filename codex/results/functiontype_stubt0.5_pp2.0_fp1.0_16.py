from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))

print(type(a.close))
print(type(a.send))
print(type(a.throw))

print(type(a.__next__) == FunctionType)
print(type(a.__iter__) == FunctionType)

print(type(a.close) == FunctionType)
print(type(a.send) == FunctionType)
print(type(a.throw) == FunctionType)

print(type(a.__next__) == MethodType)
print(type(a.__iter__) == MethodType)

print(type(a.close) == MethodType)
print(type(a.send) == MethodType)
print(type(a.throw) == MethodType)

print(type(a.__next__) == type)
print(type(a.__iter__) == type)

print(type(a.close) == type)
print(type(a.send) == type)
print
