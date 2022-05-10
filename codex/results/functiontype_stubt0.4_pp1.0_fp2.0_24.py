from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)
print(a == (x for x in [1]))

print(a)
print(a.gi_frame.f_code.co_name)
print(a.gi_frame.f_code.co_filename)
print(a.gi_frame.f_code.co_firstlineno)
print(a.gi_frame.f_code.co_argcount)
print(a.gi_frame.f_code.co_varnames)
print(a.gi_frame.f_code.co_freevars)
print(a.gi_frame.f_code.co_cellvars)

print(a.gi_frame.f_lasti)
print(a.gi_frame.f_lineno)
print(a.gi_frame.f_locals)
print(a.gi_frame.f_trace)

print(a.gi_frame.f_back)

print(a.gi_
