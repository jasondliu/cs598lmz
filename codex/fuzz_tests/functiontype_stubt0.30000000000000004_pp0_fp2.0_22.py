from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

b = (x for x in [1])
print(b.gi_frame)
print(b.gi_frame.f_code)
print(b.gi_frame.f_code.co_name)
print(b.gi_frame.f_code.co_filename)
print(b.gi_frame.f_code.co_firstlineno)
print(b.gi_frame.f_code.co_varnames)
print(b.gi_frame.f_code.co_argcount)
print(b.gi_frame.f_code.co_flags)
print(b.gi_frame.f_code.co_code)
print(b.gi_frame.f_code.co_consts)
print(b.gi_frame.f_code.co_names)
print(b.gi_frame.f_code.co_lnotab)
print(b.gi_frame.f_code.co
