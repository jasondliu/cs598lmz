from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
# 
# CodeType(argcount, nlocals, stacksize, flags, codestring, constants, names, varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])
# 
# Return a new code object. Not for the faint of heart.
# 
# The code object returned by this function may not be able to execute in an environment where the freevars and cellvars names (the variables that are used by nested functions) are not in the globals and locals.
# 
# The code object has the following attributes:
# 
# co_argcount
# number of arguments (not including * or ** args)
# co_nlocals
# number of local variables
# co_stacksize
# virtual machine stack space required
# co_flags
# flag bits indicating whether the function uses * or ** args, and more
# co_code
# string of raw compiled bytecode
# co_consts
# tuple of constants used in the bytecode
# co_
