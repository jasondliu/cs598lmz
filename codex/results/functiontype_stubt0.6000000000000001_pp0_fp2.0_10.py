from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
c = a
print(a == b)
print(a == c)
print(isinstance(a, FunctionType))
print(type(a))
print(dir(a))

print(a.gi_frame)
print(a.gi_running)
print(a.gi_code)
print(a.gi_frame.f_locals)
print(a.gi_frame.f_globals)
print(a.gi_frame.f_back)
