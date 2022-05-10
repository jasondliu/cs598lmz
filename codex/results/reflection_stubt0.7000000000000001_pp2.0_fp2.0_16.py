fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
 
# Output:
# Traceback (most recent call last):
#   File "main.py", line 7, in <module>
#     fn()
# TypeError: 'code' object is not callable
 
# We can define a custom code object, but it needs to implement the __call__ method.
 
import types
 
class Code:
    def __init__(self, argcount, kwonlyargcount, nlocals, stacksize, flags, codestring,
                 constants, names, varnames, filename, name, firstlineno, lnotab,
                 freevars, cellvars):
        self.argcount = argcount
        self.kwonlyargcount = kwonlyargcount
        self.nlocals = nlocals
        self.stacksize = stacksize
        self.flags = flags
        self.codestring = codestring
        self.constants = constants
        self.names = names
        self.varnames = varnames
        self.filename = filename
        self.name = name
        self
