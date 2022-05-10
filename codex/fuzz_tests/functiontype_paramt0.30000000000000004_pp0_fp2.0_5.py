from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# FunctionType(code, globals, name, argdefs, closure)
# code: the compiled code object
# globals: the global namespace in which the function is defined
# name: the name of the function
# argdefs: the default values for the function's arguments
# closure: a tuple of cells that contain bindings for the function's free variables

# The code object is the same as the code object for a function definition.
# The globals argument is the global namespace in which the function is defined.
# The name argument is the name of the function.
# The argdefs argument is a tuple of default values for the function's arguments.
# The closure argument is a tuple of cells that contain bindings for the function's free variables.

# The function's __globals__ attribute is the globals argument.
# The function's __name__ attribute is the name argument.
# The function's __defaults__ attribute is the argdefs argument.
# The function's __closure__ attribute is the closure argument.
# The function's __code__ attribute is the code object
