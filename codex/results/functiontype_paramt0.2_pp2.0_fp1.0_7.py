from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
# CodeType(argcount, nlocals, stacksize, flags, codestring, constants, names,
#          varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])

# argcount is the number of arguments (including arguments with default values and keyword-only arguments)
# nlocals is the number of local variables used by the function (including arguments)
# stacksize is the required stack size (including local variables)
# flags is an integer encoding a number of flags for the interpreter
# codestring is the string of raw compiled bytecode
# constants is a tuple containing the literals used by the bytecode
# names is a tuple containing the names used by the bytecode
# varnames is a tuple containing the names of the local variables (starting with the argument names)
# filename is the filename from which the code was compiled
# name is the name with which the code was defined
# firstlineno is the first line number of the function
# lnotab is a string encoding the mapping from bytecode offsets
