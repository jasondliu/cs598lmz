from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['<lambda>']

# The code object is a read-only object that contains the bytecode that implements the function body.
# The co_varnames attribute is a tuple containing the names of the local variables (including arguments).
# The co_argcount attribute contains the number of arguments (excluding * and ** args).

# The function object is a wrapper around the code object.
# It contains a dictionary for the function’s global and local namespace.
# It also contains a reference to the function object of the enclosing scope (the global scope in this case).
# The function object is the runtime context for executing the function body.

# The function object is created when the function definition is executed.
# The function object is passed as the first argument to the code object when the function is called.
# The function object is also available as the __globals__ attribute of the code object.

# The function object is the runtime context for executing the function body.
# The function object is passed as the first argument to the code object when the function is called.

