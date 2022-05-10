from types import FunctionType
a = (x for x in [1])

print(type(a))
print(a)
print(type(sum))
print(isinstance(sum, FunctionType))
print(sum)

print(type(abs))
print(abs)
print(isinstance(abs, FunctionType))
