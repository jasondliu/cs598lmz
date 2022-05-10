from types import FunctionType
list(FunctionType(0,0,0))

# CodeType
class CodeType(object):
    def __init__(self, argcount, nlocals, stacksize, flags, codestring, constants, names, varnames, filename, name, firstlineno, lnotab, freevars, cellvars):
        self.argcount = argcount
        self.nlocals = nlocals
        self.stacksize = stacksize
        self.flags = flags
        self.codestring = codestring
        self.constants = constants
        self.names = names
        self.varnames = varnames
        self.filename = filename
        self.name = name
        self.firstlineno = firstlineno
        self.lnotab = lnotab
        self.freevars = freevars
        self.cellvars = cellvars
    def __repr__(self):
        return "types.CodeType"
    def __str__(self):
        return "types.CodeType"
    def __len__(self):
        return 0
    def __
