from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
c = a

print('a is b: ', a is b)
print('a is c: ', a is c)
print('a is FunctionType: ', isinstance(a, FunctionType))
