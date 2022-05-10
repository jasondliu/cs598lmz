from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))

a = [x for x in [1]]
print(type(a))
print(isinstance(a, list))

a = {x for x in [1]}
print(type(a))
print(isinstance(a, set))

a = {1:2}
print(type(a))
print(isinstance(a, dict))

a = FunctionType(lambda : 1, {})
print(type(a))
print(isinstance(a, FunctionType))

a = type(1)
print(type(a))
print(isinstance(a, type))

a = type(lambda : 1)
print(type(a))
print(isinstance(a, type))

a = type(type(1))
print(type(a))
print(isinstance(a, type))

a = type(type(lambda : 1))
print(type(a))
print(isinstance(a, type))

a = type(type(type(1)))
print
