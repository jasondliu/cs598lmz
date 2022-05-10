fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #24074: Do not crash when __code__ is a custom object.
class Code:
    def __init__(self, argcount, kwonlyargcount, nlocals, stacksize, flags,
                 code, constants, names, varnames, filename, name, firstlineno,
                 lnotab, freevars, cellvars):
        self.co_argcount = argcount
        self.co_kwonlyargcount = kwonlyargcount
        self.co_nlocals = nlocals
        self.co_stacksize = stacksize
        self.co_flags = flags
        self.co_code = code
        self.co_consts = constants
        self.co_names = names
        self.co_varnames = varnames
        self.co_filename = filename
        self.co_name = name
        self.co_firstlineno = firstlineno
        self.co_lnotab = lnotab
        self.co_freevars = freevars
        self
