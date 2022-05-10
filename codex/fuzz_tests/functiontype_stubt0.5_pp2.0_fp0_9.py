from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, GeneratorType))

a = [x for x in [1]]
print(a)
print(type(a))
print(isinstance(a, GeneratorType))

a = {x for x in [1]}
print(a)
print(type(a))
print(isinstance(a, GeneratorType))

a = {x: x for x in [1]}
print(a)
print(type(a))
print(isinstance(a, GeneratorType))

a = FunctionType(lambda x: x, globals())
print(a)
print(type(a))
print(isinstance(a, FunctionType))
