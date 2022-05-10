from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
# CodeType(argcount, nlocals, stacksize, flags, codestring, constants, names,
#          varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])
#
# argcount: number of arguments (including arguments with default values and * or ** args)
# nlocals: number of local variables used by the function (including arguments)
# stacksize: virtual machine stack space required (ignored by the CPython interpreter)
# flags: flag bits indicating how the function was compiled (see below)
# codestring: string of raw compiled bytecode
# constants: tuple of constants used by the bytecode
# names: tuple of names used by the bytecode
# varnames: tuple of local variable names
# filename: name of file in which the code was compiled
# name: name with which the code was defined
# firstlineno: number of first line in Python source code
# lnotab: string encoding bytecode to line number mapping
# freevars: tuple of names of free
