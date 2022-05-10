from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, list))
print(isinstance(a, tuple))
print(isinstance(a, dict))
print(isinstance(a, set))
print(isinstance(a, frozenset))

print(dir(a))

print(a.gi_code)
print(a.gi_frame)
print(a.gi_running)
print(a.gi_yieldfrom)

# print(a.gi_code.co_name)
# print(a.gi_code.co_argcount)
# print(a.gi_code.co_consts)
# print(a.gi_code.co_varnames)
# print(a.gi_code.co_names)
# print(a.gi_code.co_filename)
# print(a.gi_code.co_firstlineno)
# print(a.gi_code.co_lnotab)
# print(a.
