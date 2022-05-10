from types import FunctionType
a = (x for x in [1])
b = FunctionType(a.gi_code, a.gi_frame.f_globals)
b.__kwdefaults__ = a.gi_kwdefaults
b = b(1)
print(b)
