from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
c = a
print(a is b, a is c, type(a))
print(type(a) is not FunctionType)
