from types import FunctionType
list(FunctionType(lambda x: x ** 2, globals(), 'square')(3))

# lambda x: x ** 2 is a lambda expression that returns the square of its argument.
# FunctionType is the constructor for function objects.
# globals() is a dictionary containing the global variables in the current module.
# 'square' is the name of the function.

# The lambda expression is the first argument. The second argument is a dictionary that
# contains the function's global variables (the global namespace). The last argument is
# the function's name.

# FunctionType objects are callable. The function object created by FunctionType is
# called square. It returns the square of its argument.

# The lambda expression and the FunctionType constructor are not part of the Python
# language. They are part of the CPython implementation.

# The FunctionType constructor is not documented.

# However, you can use the __code__ attribute of a function object to get a code object
# for the function body. You can create a function object from a code object using the
# code object's __new__ method.

# You can use the __code__ attribute of a
