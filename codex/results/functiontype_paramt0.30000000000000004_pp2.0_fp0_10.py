from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# The following is the same as the above, but uses the function type constructor
# directly.
FunctionType(lambda x: x, globals(), 'lambda')

# The following is the same as the above, but uses the function type constructor
# directly and uses the default name.
FunctionType(lambda x: x, globals())

# The following is the same as the above, but uses the function type constructor
# directly and uses the default globals.
FunctionType(lambda x: x)

# The following is the same as the above, but uses the function type constructor
# directly and uses the default globals and name.
FunctionType(lambda x: x)

# The following is the same as the above, but uses the function type constructor
# directly and uses the default globals, name, and code.
FunctionType(lambda x: x)

# The following is the same as the above, but uses the function type constructor
# directly and uses the default globals, name, code, and defaults.
FunctionType(lambda x: x)

# The following
