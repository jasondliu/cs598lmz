from types import FunctionType
a = (x for x in [1])
b = [1, 2, 3]
c = lambda x:x
print(type(a) is GeneratorType)
print(type(b) is list)
print(type(c) is FunctionType)
