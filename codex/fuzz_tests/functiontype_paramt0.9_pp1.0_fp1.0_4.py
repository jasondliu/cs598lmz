from types import FunctionType
list(FunctionType(lambda x:x**2, {}).__closure__)

# This is how you find the default parameters of a function:
# FunctionType(f).__defaults__
