gi = (i for i in ())
# Test gi.gi_code
def f(): pass
assert f.__code__.co_filename == __file__

# Test __code__ attribute on code objects
def f(): pass
assert f.__code__.__code__ is f.__code__

# Test code_new
def g(): pass
code_new_co = code.co_code(g.__code__)
def f():
    pass
assert code.code_new(f.__code__.co_argcount, f.__code__.co_kwonlyargcount,
f.__code__.co_nlocals, f.__code__.co_stacksize, f.__code__.co_flags,
code_new_co, f.__code__.co_consts, f.__code__.co_names, f.__code__.co_varnames,
f.__code__.co_filename, f.__code__.co_name, f.__code__.co_firstlineno,
f.__code__.co_lnotab, f.__code__.co_freevars
