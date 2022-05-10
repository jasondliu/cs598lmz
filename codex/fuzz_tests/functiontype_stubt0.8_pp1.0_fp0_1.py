from types import FunctionType
a = (x for x in [1])
print(a, type(a))
f = lambda x: x
print(f, type(f))
g = FunctionType(f.__code__, f.__globals__, name="g",
                 argdefs=(), closure=())
print(g, type(g))

# the next is not a function, it's a generator.
h = FunctionType(a.gi_code, a.gi_frame.f_globals, name="h",
                 argdefs=(), closure=())
print(h, type(h))
print(h())
# <generator object <genexpr> at 0x02ECFED0> <class 'generator'>
# <function <lambda> at 0x02F00D68> <class 'function'>
# <function g at 0x02F00DF0> <class 'function'>
# <function h at 0x02F00D18> <class 'function'>
# <generator object h at 0x02ECFED0>
