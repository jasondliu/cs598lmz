from types import FunctionType
a = (x for x in [1])
b = (x for x in [1, 2])
print(a)
print(b)
print(a.gi_frame)
print(b.gi_frame)
print(a.gi_running)
print(b.gi_running)
print(a.gi_code)
print(b.gi_code)

print(a.gi_frame.f_lasti)
print(b.gi_frame.f_lasti)

print(a.gi_frame.f_code.co_filename)
print(b.gi_frame.f_code.co_filename)

print(a.gi_frame.f_code.co_name)
print(b.gi_frame.f_code.co_name)

print(a.gi_frame.f_code.co_argcount)
print(b.gi_frame.f_code.co_argcount)

print(a.gi_frame.f_code.co_argcount)
print(b.gi_frame.f_code.co_argcount)

print(a
