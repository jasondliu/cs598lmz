from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
# CodeType(argcount, nlocals, stacksize, flags, codestring, constants, names,
#          varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])
#
# argcount: number of arguments (including arguments with default values and
#           keyword-only arguments)
# nlocals: number of local variables used by the function (including arguments)
# stacksize: virtual machine stack space required (only a hint)
# flags: bitmap, encoding various information about the code
# codestring: string of bytes encoding the Python bytecode
# constants: tuple of objects used by the bytecode
# names: tuple of strings, giving names used by the bytecode
# varnames: tuple of strings, giving local variable names
# filename: string, name of file in which this code was compiled
# name: string, name with which this code was defined
# firstlineno: first line number of the function
# lnotab: string encoding mapping of line numbers to bytecode indices
# free
