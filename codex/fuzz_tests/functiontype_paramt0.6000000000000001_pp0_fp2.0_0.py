from types import FunctionType
list(FunctionType(lambda x: x+1, globals(), "lambda"))

# FunctionType(code, globals, name) -> function object
# FunctionType(code, globals, name, argdefs, closure) -> function object

# Create a function with a given code object.  The optional name
# string overrides the name from the code object.  The optional
# argdefs tuple specifies the default argument values.  The optional
# closure tuple supplies the bindings for free variables.
#
# When the code object is executed, the bindings for the free variables
# are looked up in the globals, followed by the closure.  If a free
# variable is not found in either, a NameError is raised.
#
# WARNING: Many Python implementations don't support passing closures
# into functions.  Portable programs should only use globals.

# Function attributes:
# __doc__         docstring
# __name__        name with which this function was defined
# __dict__        dictionary for instance variables (if defined)
# __defaults__    tuple of any default values for arguments
# __globals__     global namespace in which this function
