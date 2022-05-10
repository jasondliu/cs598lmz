from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

b = lambda x: x+1
print(b)
print(type(b))

print(FunctionType)
