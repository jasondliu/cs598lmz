from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
# CodeType(argcount, nlocals, stacksize, flags, codestring, constants, names,
#          varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])
#
# argcount: the number of arguments (including arguments with default values and
#           those arguments passed by keyword).
# nlocals: the number of local variables used by the function (including arguments).
# stacksize: the required stack size (including local variables).
# flags: compiler and interpreter flags.
# codestring: a string representing the sequence of bytecode instructions.
# constants: a tuple containing the literals used by the bytecode.
# names: a tuple containing the names used by the bytecode.
# varnames: a tuple containing the names of local variables (starting with the
#           argument names).
# filename: the filename from which the code was compiled.
# name: the name with which the code object was defined.
# firstlineno: the first line number of the function.
# lnot
