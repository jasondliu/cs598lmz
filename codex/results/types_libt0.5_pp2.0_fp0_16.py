import types
types.FunctionType(lambda: None, globals())

# Function types can be created using the FunctionType constructor.

# The first argument is a code object, and the second is a dictionary that
# should be used as the global namespace when the code is executed.

# This example creates the same function as above.

# The code object is retrieved from the function using __code__.

# The globals dictionary is the same dictionary that is returned by
# globals().

# The code object is a read-only attribute that contains the compiled version
# of the function body.

# The globals dictionary is used to resolve global references.

# The __globals__ attribute of the function contains the global namespace that
# is used.

# For functions created using the lambda statement, the globals dictionary is
# not used.

# The function has access to the global namespace where it was defined, but no
# other global namespaces.

# The globals dictionary of the function contains the same namespace as the
# globals() function would return for the same code.
