from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)
print(type(a) == list)

print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, list))

print(isinstance(a, (GeneratorType, FunctionType, list)))

print(dir(a))

print(a.gi_frame)
print(a.gi_code)
print(a.gi_running)
print(a.gi_yieldfrom)

print(a.__next__())
print(a.__next__())

print(a.gi_frame)
print(a.gi_code)
print(a.gi_running)
print(a.gi_yieldfrom)
