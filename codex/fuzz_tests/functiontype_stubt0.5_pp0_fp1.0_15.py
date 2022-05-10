from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(dir(a))
print('-' * 40)

print(a.gi_code)
print(type(a.gi_code))
print(dir(a.gi_code))
print(a.gi_code.co_name)
print('-' * 40)

print(a.gi_frame)
print(type(a.gi_frame))
print(dir(a.gi_frame))
print('-' * 40)

print(a.gi_running)
print(type(a.gi_running))
print(dir(a.gi_running))
print('-' * 40)

print(a.gi_yieldfrom)
print(type(a.gi_yieldfrom))
print(dir(a.gi_yieldfrom))
print('-' * 40)
