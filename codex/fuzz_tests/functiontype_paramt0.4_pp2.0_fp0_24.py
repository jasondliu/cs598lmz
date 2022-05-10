from types import FunctionType
list(FunctionType(lambda x: x + 1, globals())(x) for x in range(5))

# [1, 2, 3, 4, 5]

# Note that the second argument to FunctionType is the global namespace.
# This is used to resolve the reference to the built-in function len().
# If you were to pass in a different namespace, then you would get an error:

list(FunctionType(lambda x: x + 1, {})(x) for x in range(5))

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <genexpr>
# NameError: global name 'len' is not defined

# You can also use this to create a function that has a different global namespace:

list(FunctionType(lambda x: x + 1, {})(x) for x in range(5))

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <genexpr
