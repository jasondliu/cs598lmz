from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, 'f', f.func_defaults, f.func_closure))

# Same, but without closure
list(FunctionType(f.func_code, f.func_globals, 'f', f.func_defaults))

# Same, but without default arguments
list(FunctionType(f.func_code, f.func_globals, 'f'))

def f(a, b=10, *c, **d):
    return a, b, c, d

f.__defaults__
f.__kwdefaults__
