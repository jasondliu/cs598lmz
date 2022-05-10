from types import FunctionType
list(FunctionType(lambda: 0, {}).__code__.co_varnames)

# ['__builtins__', '__name__', '__doc__', '__package__']

# The code object is a read-only object that contains the bytecode for the function.
# It is created when the function is defined and cannot be modified.
# The bytecode is a sequence of instructions that the interpreter executes to run the function.
# The bytecode is not necessarily the same across Python implementations.
# The bytecode is not necessarily the same even for the same Python implementation
# if the function is defined in a module that is imported by different means.
# For example, if the module is imported normally or through zipimport.
# The bytecode can be inspected using the dis module.

# The code object has a co_varnames attribute that is a tuple containing the names of the local variables
# used by the function, including arguments.
# The first items in the tuple are the argument names.
# The rest are the local variables.
# The names of the global and built-in variables used by the function are not included.

# The code object also
