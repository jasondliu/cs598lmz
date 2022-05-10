from types import FunctionType
a = (x for x in [1])
print(type(a)==FunctionType)

print(dir(a))
print(type(a))
