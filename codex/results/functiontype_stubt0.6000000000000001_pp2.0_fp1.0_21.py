from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))

b = (x for x in [1])
print(type(b.gi_frame))
print(b.gi_frame.f_code)
print(b.gi_frame.f_code.co_name)

c = (x for x in [1])
print(c.gi_frame.f_locals)

d = (x for x in [1])
print(d.gi_frame.f_trace)
print(d.gi_frame.f_trace is None)

e = (x for x in [1])
print(e.gi_frame.f_lasti)
print(e.gi_frame.f_lineno)

f = (x for x in [1])
print(f.gi_frame.f_back)

g = (x for x in [1])
print(g.gi_frame.f_back is None)

h = (x for x in [1])
print(h.gi_frame.f_builtins)
