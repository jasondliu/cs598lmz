from types import FunctionType
list(FunctionType(x,globals(),'foo'))

# code objects
# ------------

# code objects are immutable and contain no references to anything outside
# of the code object itself.

# code objects are created by the compiler and executed by the interpreter.

# code objects are also returned by built-in functions like compile() and
# the various opcode functions.

# code objects have a number of attributes:
#
# co_argcount     number of arguments (not including * or ** args)
# co_nlocals      number of local variables
# co_stacksize    virtual machine stack space required
# co_flags        bitmap: 1=optimized | 2=newlocals | 4=*arg | 8=**arg
# co_code         string of bytes encoding the bytecode instructions
# co_consts       tuple of constants used in the bytecode
# co_names        tuple of names of local variables
# co_varnames     tuple of names of arguments and local variables
# co_filename     name of file in which this code object was created
# co_name         name with which this code object was defined

