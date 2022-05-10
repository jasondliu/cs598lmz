from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) is GeneratorType)
print(type(a) is tuple)
print(type(a) is FunctionType)
