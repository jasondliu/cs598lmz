from types import FunctionType
list(FunctionType(lambda: 1, {}).__code__.co_consts)

# Code object attributes:
# co_argcount: number of arguments (not including * or ** args)
# co_cellvars: tuple of names of local variables that are referenced by nested functions
# co_code: string representing the sequence of bytecode instructions
# co_consts: tuple of constants used in the bytecode
# co_filename: name of file in which this code object was created
# co_firstlineno: number of first line in Python source code
# co_flags: bitmap: 1=optimized | 2=newlocals | 4=*args | 8=**kwargs | 16=nested
# co_lnotab: encoded mapping of line numbers to bytecode indices
# co_name: name with which this code object was defined
# co_names: tuple of names of local variables
# co_nlocals: number of local variables
# co_stacksize: virtual machine stack space required
# co_varnames: tuple of names of arguments and local variables
# co_freevars: tuple of names of free variables

