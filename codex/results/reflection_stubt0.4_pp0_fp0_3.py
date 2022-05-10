fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #13774: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = object()
f()

# Issue #14104: segfault when __code__ is a code object but not a PyCodeObject
class Code(object):
    def __init__(self, argcount, kwonlyargcount, nlocals, stacksize, flags,
                 code, consts, names, varnames, filename, name, firstlineno,
                 lnotab, freevars, cellvars):
        self.co_argcount = argcount
        self.co_kwonlyargcount = kwonlyargcount
        self.co_nlocals = nlocals
        self.co_stacksize = stacksize
        self.co_flags = flags
        self.co_code = code
        self.co_consts = consts
        self.co_names = names
        self.co_varnames = varnames
        self.co_filename = filename
        self.co_
