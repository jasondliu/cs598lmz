from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# The __closure__ attribute is a tuple of cells that contain bindings for the function’s free variables.
# A cell is a Python object that manages the environment where the function was defined.
# The __code__ attribute is an object containing the compiled function bytecode.
# The __defaults__ attribute is a tuple containing default argument values for those arguments that have defaults.
# The __globals__ attribute is a reference to the dictionary that provides global namespace for the function.
# The __dict__ attribute is the namespace supporting arbitrary function attributes.

# The __code__ attribute is an object containing the compiled function bytecode.
# The __code__ object has attributes that reveal details about the function.
# The co_varnames attribute is a tuple containing the names of the local variables (including arguments).
# The co_argcount attribute is the number of arguments (excluding * and ** arguments).

# The __defaults__ attribute is a tuple containing default argument values for those arguments that have defaults.
# The __kwdefaults__ attribute is a dictionary containing keyword-only arguments with a default value.

