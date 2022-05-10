from types import FunctionType
a = (x for x in [1])
print(type(a))

b = FunctionType(a.gi_code, a.gi_frame.f_globals, a.gi_name, a.gi_frame.f_locals)
print(type(b))

c = b()
print(type(c))

print(c.gi_code)
print(c.gi_frame)
print(c.gi_name)
print(c.gi_frame)

print(c.gi_frame.f_locals)
print(c.gi_frame.f_globals)

print(c.gi_frame.f_locals is a.gi_frame.f_locals)
print(c.gi_frame.f_globals is a.gi_frame.f_globals)

print(c.gi_frame.f_locals is b.__globals__)
print(c.gi_frame.f_globals is b.__globals__)

print(c.gi_frame.f_locals is b.__closure__
