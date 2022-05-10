from types import FunctionType
a = (x for x in [1])
b = (y for y in [1])
print(a)
print(b)

print('a is b:', a is b)

print(type(a))
print(type(b))
print(type(dir))
print(FunctionType is type(dir))
print(FunctionType is type)
