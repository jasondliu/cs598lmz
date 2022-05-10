from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(dir(a))
print(a.gi_frame.f_code)
print(a.gi_frame.f_code.co_name)
print(a.gi_frame.f_code.co_varnames)
print(a.gi_frame.f_code.co_argcount)
print(a.gi_frame.f_locals)
print(a.gi_frame.f_globals)
print(a.gi_frame.f_back)

print(a.gi_frame.f_code.co_code)
print(a.gi_frame.f_code.co_consts)
print(a.gi_frame.f_code.co_names)
print(a.gi_frame.f_code.co_varnames)
print(a.gi_frame.f_code.co_freevars)
print(a.gi_frame.f_code.co_cellvars
