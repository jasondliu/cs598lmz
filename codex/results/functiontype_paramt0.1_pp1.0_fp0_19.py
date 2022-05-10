from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
# CodeType(argcount, nlocals, stacksize, flags, codestring, constants, names,
#          varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])
#
# argcount: number of arguments (including arguments with default values and
#           keyword-only arguments)
# nlocals: number of local variables used by the function (including arguments)
# stacksize: virtual machine stack space required (ignored by the CPython
#            compiler)
# flags: bitmap of flags, see below
# codestring: string of raw compiled bytecode
# constants: tuple of constants used by the bytecode
# names: tuple of names used by the bytecode
# varnames: tuple of local variable names
# filename: name of file in which this code was compiled to bytecode
# name: name with which this code was defined
# firstlineno: number of first line in Python source code
# lnotab: string encoding bytecode-to-source code mapping
# freevars
