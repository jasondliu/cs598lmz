from types import FunctionType
a = (x for x in [1])
print(a)
b = FunctionType(a, 'b')
b()

print(type(a))
print(type(b))
print(type(b()))
