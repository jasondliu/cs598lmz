from types import FunctionType
list(FunctionType(f.func_code, globals(), "clock").__dict__.keys())

# 2. make a new func, rebind attrs
f = FunctionType(f.func_code, globals(), "anotherfunc")
dir(f)
f.__doc__

def f(a, b, c=3, *d): pass
    
# eval(f.func_args)
#eval(f.func_code)

print f.func_code.co_argcount
print f.func_code.co_varnames
print f.func_code.co_code
print f.func_code.co_flags

import dis
dis.dis(f.func_code)
