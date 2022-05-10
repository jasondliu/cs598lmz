from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['__closure__', '__code__', '__defaults__', '__dict__', '__doc__', '__globals__', '__name__', '__qualname__']

# __closure__ is the tuple of cells that contain bindings for the function’s free variables.
# __code__ is the compiled function bytecode.
# __defaults__ is the tuple of default argument values.
# __dict__ is the namespace supporting arbitrary function attributes.
# __doc__ is the docstring.
# __globals__ is the global namespace of the module that defined the function.
# __name__ is the function name.
# __qualname__ is the qualified name of the function.

# The __code__ attribute is a read-only attribute that returns a code object representing the compiled function bytecode.
# The code object has its own set of attributes, which are all read-only:

# co_argcount is the number of positional arguments (including arguments with default values).
# co_cellvars is the tuple of names
