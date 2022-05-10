from types import FunctionType
list(FunctionType(lambda x: x * 2, globals(), "lambda"))

# [<function <lambda> at 0x7f4b4c4f4e18>, <function <lambda> at 0x7f4b4c4f4ea0>]

# But, you can also do this:
list(FunctionType(lambda x: x * 2, globals(), "lambda"))

# [<function <lambda> at 0x7f4b4c4f4e18>, <function <lambda> at 0x7f4b4c4f4ea0>]

# This is because the second argument is a mapping or a dictionary. So, it's
# possible to pass a dictionary to the second argument.

# Let's see how we can do that:

# >>> def make_function(name):
# ...     return FunctionType(lambda x: x * 2, {name: "function"}, name)
# ...
# >>> make_function("test")
# <function test at 0x7f4b4c4f4f28>

# Let's see what's in the globals() of
