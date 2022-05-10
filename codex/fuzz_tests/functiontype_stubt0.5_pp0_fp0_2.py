from types import FunctionType
a = (x for x in [1])
b = (x for x in [1, 2, 3])

print(a)
print(a.gi_code.co_argcount)
print(a.gi_frame.f_lasti)
print(a.gi_frame.f_locals)
print(a.gi_frame.f_locals['x'])
print(a.gi_frame.f_trace)
print(a.gi_running)
print(a.gi_code.co_name)
print(a.gi_frame.f_lasti)
print(a.gi_frame.f_trace)
print(a.gi_frame.f_trace.__class__)
print(a.gi_frame.f_trace.__class__.__name__)
print(a.gi_frame.f_trace.__class__.__mro__)
print(a.gi_frame.f_trace.__class__.__mro__[0].__name__)
print(a.gi_frame.f_trace.__class__.__mro__[1].__
