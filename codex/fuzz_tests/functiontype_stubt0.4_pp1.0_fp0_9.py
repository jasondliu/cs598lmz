from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
print(a)
print(b)
print(a.gi_code)
print(b.gi_code)
print(type(a))
print(type(b))
print(type(a.gi_code))
print(type(b.gi_code))
print(a.gi_code is b.gi_code)
print(type(a.gi_frame))
print(type(b.gi_frame))
print(a.gi_frame is b.gi_frame)
print(a.gi_running)
print(b.gi_running)
print(a.gi_frame.f_lasti)
print(b.gi_frame.f_lasti)
print(a.gi_frame.f_lasti is b.gi_frame.f_lasti)
print(a.gi_frame.f_locals)
print(b.gi_frame.f_locals)
print(a.gi_frame.f_locals is b.gi_frame.f_locals)
print(a
