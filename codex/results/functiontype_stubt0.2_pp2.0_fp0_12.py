from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(dir(a))

print(a.gi_frame)
print(a.gi_code)
print(a.gi_running)
print(a.gi_yieldfrom)

print(a.gi_frame.f_locals)
print(a.gi_frame.f_code.co_name)
print(a.gi_frame.f_code.co_varnames)
print(a.gi_frame.f_code.co_argcount)
print(a.gi_frame.f_code.co_argnames)
print(a.gi_frame.f_code.co_filename)
print(a.gi_frame.f_code.co_firstlineno)
print(a.gi_frame.f_code.co_lnotab)
print(a.gi_frame.f_code.co_flags)
print(a.gi_frame.f_code.co_freevars)

