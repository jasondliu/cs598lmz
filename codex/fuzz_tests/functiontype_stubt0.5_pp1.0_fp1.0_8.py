from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(a.gi_frame)
print(a.gi_code)
print(a.gi_frame.f_code)
print(a.gi_frame.f_code == a.gi_code)

print(a.gi_frame.f_locals)
print(a.gi_frame.f_locals['x'])

print(a.gi_frame.f_lasti)
print(a.gi_frame.f_lineno)
print(a.gi_frame.f_back)

print(a.gi_frame.f_code.co_freevars)
print(a.gi_frame.f_code.co_varnames)
print(a.gi_frame.f_code.co_name)
print(a.gi_frame.f_code.co_filename)
print(a.gi_frame.f_code.co_firstlineno)

print(a.gi_frame
