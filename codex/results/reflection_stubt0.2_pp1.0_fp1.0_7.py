fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_attributes
def f():
    pass

f.__code__.co_argcount
f.__code__.co_cellvars
f.__code__.co_code
f.__code__.co_consts
f.__code__.co_filename
f.__code__.co_firstlineno
f.__code__.co_flags
f.__code__.co_freevars
f.__code__.co_kwonlyargcount
f.__code__.co_lnotab
f.__code__.co_name
f.__code__.co_names
f.__code__.co_nlocals
f.__code__.co_stacksize
f.__code__.co_varnames

# test_code_compare
def f():
    pass

def g():
    pass

f.__code__ == g.__code__
f.__code__ != g.__code__

# test_code_richcompare
def f():

