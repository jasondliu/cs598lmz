from types import FunctionType
a = (x for x in [1])
print(type(a))
print(dir(a))

print('\n\n')

print(dir(FunctionType))
print(dir(type))
print(dir(list))
print(dir(tuple))
