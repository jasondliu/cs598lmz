fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_attributes
def f(x):
    """doc"""
    return x
f.__code__.co_argcount
f.__code__.co_consts
f.__code__.co_filename
f.__code__.co_firstlineno
f.__code__.co_flags
f.__code__.co_lnotab
f.__code__.co_name
f.__code__.co_names
f.__code__.co_nlocals
f.__code__.co_stacksize
f.__code__.co_varnames

# test_cell_attributes
def f(x):
    def g(y):
        return x + y
    return g
f(1).__closure__[0].cell_contents

# test_frame_attributes
def f(x):
    """doc"""
    return x
def g(y):
    return f(y)
g.__code__.co_filename
g.__code__.co_first
