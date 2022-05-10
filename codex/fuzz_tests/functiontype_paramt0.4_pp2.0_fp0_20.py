from types import FunctionType
list(FunctionType(f.__code__, globals(), "foo"))

# Code objects can be executed or evaluated with the built-in functions exec() and eval().

# The exec() function takes a code object and optional globals and locals.
# If provided, globals must be a dictionary.
# If provided, locals can be any mapping object.
# Unknown names are looked up in globals and locals.
# Names in locals take precedence over names in globals.
# If no globals and locals are provided, the globals and locals where exec() is called are used.
# If only globals is provided, it must be a dictionary.
# In this case, locals defaults to globals.
# If globals and locals are omitted, they default to the globals and locals of the scope where exec() is called.
# If only locals is provided, it must be a mapping object.
# In this case, globals defaults to locals.

# If the globals dictionary does not contain a value for the key __builtins__, a reference to the dictionary of the built-in module builtins is inserted under that key before expression is parsed.
# This means that
