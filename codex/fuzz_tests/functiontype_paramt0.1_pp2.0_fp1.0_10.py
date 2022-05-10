from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
# CodeType(argcount, nlocals, stacksize, flags, codestring, constants, names,
#          varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])

# argcount
# The number of arguments (including arguments with default values, * and **
# arguments) the function takes.

# nlocals
# The number of local variables used by the function (including arguments).

# stacksize
# The required stack size (including local variables).

# flags
# The flag bits are:

# 0x04 - Function takes variable number of arguments
# 0x08 - Function uses the *arguments syntax to accept other arguments
# 0x20 - Function is a generator
# 0x40 - Function is a generator using the yield from syntax
# 0x80 - Function is an async generator
# 0x100 - Function is a coroutine
# 0x200 - Function is an async coroutine

# codestring
# The string of bytecode instructions.

#
