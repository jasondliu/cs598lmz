from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

print(a.gi_frame.f_lasti)
print(a.gi_frame.f_code.co_name)
print(a.gi_frame.f_code.co_varnames)
print(a.gi_frame.f_code.co_argcount)
print(a.gi_frame.f_code.co_flags)
print(a.gi_frame.f_code.co_filename)
print(a.gi_frame.f_code.co_firstlineno)
print(a.gi_frame.f_code.co_lnotab)
print(a.gi_frame.f_code.co_stacksize)
print(a.gi_frame.f_code.co_names)
print(a.gi_frame.f_code.co_nlocals)
print(a.gi_frame
