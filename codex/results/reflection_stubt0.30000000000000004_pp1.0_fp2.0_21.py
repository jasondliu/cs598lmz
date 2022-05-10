fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #2885: test that the new code object is properly initialized.
def f(): pass
c = f.__code__
c = types.CodeType(c.co_argcount, c.co_kwonlyargcount, c.co_nlocals, c.co_stacksize,
                   c.co_flags, c.co_code, c.co_consts, c.co_names, c.co_varnames,
                   c.co_filename, c.co_name, c.co_firstlineno, c.co_lnotab,
                   c.co_freevars, c.co_cellvars)
f.__code__ = c

# Issue #2885: test that the new code object is properly initialized.
def f(): pass
c = f.__code__
c = types.CodeType(c.co_argcount, c.co_kwonlyargcount, c.co_nlocals, c.co_stacksize,
                   c.co_flags, c.co_code
