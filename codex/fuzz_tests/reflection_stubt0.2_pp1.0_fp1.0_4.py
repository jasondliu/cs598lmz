fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_attributes
def f(): pass
f.__code__.co_filename
f.__code__.co_name
f.__code__.co_firstlineno
f.__code__.co_lnotab

# test_code_newempty
def f(): pass
code = f.__code__
code.co_argcount
code.co_kwonlyargcount
code.co_nlocals
code.co_stacksize
code.co_flags
code.co_code
code.co_consts
code.co_names
code.co_varnames
code.co_freevars
code.co_cellvars

# test_code_new
def f(x):
    y = x + 1
    return y

code = f.__code__
code.co_argcount
code.co_kwonlyargcount
code.co_nlocals
code.co_stacksize
code.co_flags
code.co_code
code.co_consts
code.co
