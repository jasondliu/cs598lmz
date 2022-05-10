from types import FunctionType
a = (x for x in [1])
b = a.gi_frame
c = FunctionType(b.f_code, b.f_globals, 'foo', b.f_defaults, b.f_closure)
c()
</code>

