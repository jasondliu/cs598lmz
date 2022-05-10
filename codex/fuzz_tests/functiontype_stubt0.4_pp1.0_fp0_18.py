from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, types.GeneratorType))
b = FunctionType(a.gi_code, a.gi_frame.f_globals, a.gi_name, a.gi_frame.f_locals)
print(b)
print(b())

print('*' * 100)

import types
from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, types.GeneratorType))
b = FunctionType(a.gi_code, a.gi_frame.f_globals, a.gi_name, a.gi_frame.f_locals)
print(b)
print(b())

print('*' * 100)

import types
from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, types.GeneratorType))
b = FunctionType(a.gi_code, a.gi_frame.f_globals, a.gi_name,
