from types import FunctionType
a = (x for x in [1])
print(type(a))
print(FunctionType)
print(type(print))
print(type(__build_class__))
print(type(type))
print(type(FunctionType))

print(type(a))
print(type(1))
print(type('1'))
print(type(type(1)))
