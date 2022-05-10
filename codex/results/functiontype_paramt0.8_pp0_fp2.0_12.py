from types import FunctionType
list(FunctionType(f.__code__, f.__globals__,name=f.__name__, argdefs=f.__defaults__,closure=f.__closure__))

def f(a,b,c=1,*args,d=3,**kwargs): return a,b,c,args,d,kwargs
f.__closure__

f.__code__

f.__code__.co_varnames

f.__code__.co_argcount

f.__defaults__

f.__kwdefaults__

f.__code__.co_nlocals

f.__code__.co_consts

f.__code__.co_names

f.__code__.co_filename

f.__code__.co_firstlineno

f.__code__.co_lnotab

def make_adder(n): return lambda x: x+n
make_adder(5).__closure__[0].cell_contents

import dis
print("dis.dis(make_adder):")
