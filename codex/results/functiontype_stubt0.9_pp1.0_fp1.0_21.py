from types import FunctionType
a = (x for x in [1])
b = [1, 2]

print(type(a) ==  function)

print(type(a) ==  FunctionType)
print(type(b) ==  FunctionType)

print(isinstance(a, function))
print(isinstance(b, function))
print(isinstance(b, FunctionType))
