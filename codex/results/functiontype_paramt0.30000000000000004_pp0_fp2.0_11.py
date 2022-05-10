from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda').__code__.co_freevars)

# ['x']

# The name of the function is 'lambda', which is the default name of a lambda
# function. The code object is a function that returns its argument.
# The free variables are the ones that are used in the function but not
# defined in it.

# The function object is a wrapper around the code object. The code object
# contains the actual bytecode instructions of the function.

# The function object also contains the default values of the arguments,
# the globals namespace, and the closure.

# The globals namespace is the namespace where the function was defined.
# The closure is the environment captured by the function.

# The function object is created by the function type. The function type
# takes the code object, the globals namespace, and the function name.

# The function type is a class that inherits from the object type.
# It has a __call__ method that executes the code object.

# The function type is a factory that creates function objects.
# The function object is the actual function
