from types import FunctionType
list(FunctionType(i.__code__,i.__globals__,i.__name__,i.__defaults__,i.__closure__)("a"))

i(closure=None,defaults=None,name="a",globals=None,code=None)

choose()

# TODO: quick question
# Use the function __call__?
# Or the function my_function?
"""I think its the __call__ function"""


"""
# TODO: explain the **kwargs and **args function
# It looks to see if something needs to be added in a specific way?
# I need to look these up in the documentation
# Might be useful for when a function calls another function
"""


"""
# TODO: explain the closure procedure
# looks to be building a new function inside of a loop
# Looks like the function passes back something — a function object?
# Looks like it returns the arguments to the {0} position within string component
"""
