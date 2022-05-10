from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
# CodeType(argcount, nlocals, stacksize, flags, codestring, constants, names,
#          varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])
#
# argcount: the number of positional arguments (including arguments with
#           default values)
# nlocals: the number of local variables used by the function (including
#          arguments)
# stacksize: the required stack size (including local variables)
# flags: compiler and interpreter flags
# codestring: string of raw compiled bytecode
# constants: tuple of constants used in the bytecode
# names: tuple of names used by the bytecode
# varnames: tuple of local variable names
# filename: name of file in which this code was compiled
# name: name with which this code was defined
# firstlineno: number of first line in Python source code
# lnotab: mapping of line numbers to bytecode indices
# freevars: tuple of free variable names
# cellvars: tuple of cell
