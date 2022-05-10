from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, name='new_fun',
                  argdefs=f.func_defaults).__closure__)
[*map(eval, f.__code__.co_freevars)]
[*map(eval, f.__code__.co_cellvars)]
[eval(c.cell_contents) for c in f.__closure__]

f.__code__.co_freevars
tuple('x')

list(map(eval, f.__code__.co_cellvars))
[*map(eval, f.__code__.co_freevars)]
f.__closure__[0].cell_contents

a = 2
f.__closure__
f.__code__.co_cellvars
f.__code__.co_freevars

f.__code__.co_varnames
f.__code__.co_argcount


import types
a = 2
b = 3
f = lambda: a + b
c = types.FunctionType(f.
