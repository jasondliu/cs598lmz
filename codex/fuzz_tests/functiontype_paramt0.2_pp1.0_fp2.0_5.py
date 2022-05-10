from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
# CodeType(argcount, nlocals, stacksize, flags, codestring, constants, names, varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])
# argcount: the number of arguments (including arguments with default values, * and ** args)
# nlocals: the number of local variables used by the function (including arguments)
# stacksize: the required stack size (only a hint)
# flags: flag bits indicating how the compiler set up the name, local and free variable storage
# codestring: a string representing the sequence of bytecode instructions
# constants: a tuple containing the literals used by the bytecode
# names: a tuple containing the names used by the bytecode
# varnames: a tuple containing the names of the local variables (starting with the argument names)
# filename: the filename from which the code was compiled
# name: the name with which the code object was defined
# firstlineno: the first line number of the function
# lnotab: a string encoding the
