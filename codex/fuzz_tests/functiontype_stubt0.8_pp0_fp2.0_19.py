from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(None))
print(type(a) == type(None))
# print(type(a) is type(None))
# print(type(a) is FunctionType)

print(a)
print(None)
print(a == None)
print(a is None)
