from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
# CodeType(argcount, nlocals, stacksize, flags, codestring, constants, names,
#          varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])
#
# argcount: number of arguments (including arguments with default values and
#           keyword-only arguments)
# nlocals: number of local variables used by the function (including arguments)
# stacksize: virtual machine stack space required (excluding local variables)
# flags: compiler flags (see below)
# codestring: string of raw compiled bytecode
# constants: tuple of constants used by the bytecode
# names: tuple of names used by the bytecode
# varnames: tuple of local variable names
# filename: name of file in which function was defined
# name: name with which function was defined
# firstlineno: number of first line in Python source code file
# lnotab: encoded mapping of line numbers to bytecode indices (see below)
# freevars: tuple of free variable names (with the
