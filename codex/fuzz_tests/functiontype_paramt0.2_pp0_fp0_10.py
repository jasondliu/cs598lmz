from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
# code(argcount, nlocals, stacksize, flags, codestring, constants, names,
#      varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])
#
# argcount: number of arguments (including arguments with default values and
#           * and ** args)
# nlocals: number of local variables used by the function (including arguments)
# stacksize: virtual machine stack space required (ignored by the CPython
#            compiler)
# flags: compiler and interpreter flags
# codestring: string of raw compiled bytecode
# constants: tuple of constants used in the bytecode
# names: tuple of names used by the bytecode
# varnames: tuple of local variable names
# filename: name of file in which this code was compiled to bytecode
# name: name with which this code object was defined
# firstlineno: number of first line in Python source code
# lnotab: encoded mapping of line numbers to bytecode indices
# freevars: tuple of free
