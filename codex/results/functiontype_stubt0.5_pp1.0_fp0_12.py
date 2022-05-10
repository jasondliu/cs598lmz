from types import FunctionType
a = (x for x in [1])
b = FunctionType(a.gi_code, a.gi_frame.f_globals, a.gi_frame.f_code.co_name, a.gi_frame.f_locals)
b()
</code>

