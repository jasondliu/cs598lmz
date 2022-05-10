from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(type(a), type(b), type(a) is type(b))
print(isinstance(a, type(b)), isinstance(b, type(a)))
print(type(a) == type(b))
print(issubclass(type(a), type(b)), issubclass(type(b), type(a)))
print(FunctionType(a.__code__, a.__globals__))

print(a.gi_code is b.gi_code)
print(a.__code__ is b.__code__)
print(a.gi_frame is b.gi_frame)
print(a.gi_running)
print(a.gi_yieldfrom)

print(next(a))
print(next(b))
print(a.gi_running)
print(a.gi_yieldfrom)

print(b.gi_running)
print(b.gi_yieldfrom)


print(a.__qualname__)
print(b
