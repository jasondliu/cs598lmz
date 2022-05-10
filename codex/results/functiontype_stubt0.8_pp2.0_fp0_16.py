from types import FunctionType
a = (x for x in [1])
f = FunctionType(a.gi_code, {}, a.gi_name, a.gi_defaults)
print [x for x in f()]
