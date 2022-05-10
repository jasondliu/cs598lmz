from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['x', 'y']

# The code object is a read-only object that contains the bytecode instructions for the function body.
# The co_varnames attribute is a tuple containing the names of the local variables used by the function.
# The co_argcount attribute contains the number of arguments the function takes.
# The co_flags attribute is an integer encoding a number of flags used internally by the interpreter.
# The co_code attribute is a string containing the sequence of bytecode instructions.
# The co_consts attribute is a tuple containing the literals used by the bytecode.
# The co_names attribute is a tuple containing the names used by the bytecode.
# The co_nlocals attribute is the number of local variables used by the function.
# The co_stacksize attribute is the required stack size.
# The co_filename attribute is the filename from which the code was compiled.
# The co_name attribute is the name of the function.
# The co_firstlineno attribute is the first line number of the function.
# The
