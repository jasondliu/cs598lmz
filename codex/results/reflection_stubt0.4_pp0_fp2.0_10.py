fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn()

# This is a regression test for a bug that caused a segfault when the
# __code__ attribute of a function was replaced with a code object
# that was not created by PyCode_New().

def f():
    pass

def g():
    pass

f.__code__ = g.__code__

# This is a regression test for a bug that caused a segfault when the
# __code__ attribute of a function was replaced with a code object
# that was created by PyCode_New() but had a NULL co_consts.

def f():
    pass

def g():
    pass

c = g.__code__
c = types.CodeType(c.co_argcount, c.co_nlocals, c.co_stacksize,
                   c.co_flags, c.co_code, c.co_consts, c.co_names,
                   c.co_varnames, c.co_filename, c.co_name,
