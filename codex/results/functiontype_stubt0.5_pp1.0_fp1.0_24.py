from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a.__name__)
print(a.__qualname__)
print(a.__dict__)
print(a.__closure__)
print(a.__code__)
print(a.__globals__)
print(a.__module__)

print(type(a))
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))

print(a == b)
print(a is b)

print(a.gi_code)
print(a.gi_frame)
print(a.gi_running)
print(a.gi_yieldfrom)
