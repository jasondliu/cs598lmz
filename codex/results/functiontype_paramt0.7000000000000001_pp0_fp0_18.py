from types import FunctionType
list(FunctionType(lambda x:x**2, globals())(i) for i in range(10))
 

# Here, we use a list comprehension to generate a list of squared numbers.
# The list comprehension has a nested expression: x:x**2.
# This nested expression creates a lambda function, which is then called
# with argument i that comes from the list comprehension.

# The list comprehension can be written as
# (FunctionType(lambda x:x**2, globals())(i) for i in range(10)).
# This can be even more confusing.

# We can also write a simple function that returns a function.
@FunctionType
def myfunc(x):
    return x**2

list(map(myfunc, range(10)))
 

# The decorator @FunctionType can also be written as FunctionType().
# This is just syntactic sugar. The decorator is only syntactic sugar for
# nested functions, that is, functions that are defined inside other functions
# and refer to variables in the enclosing scope.

# In Python, all functions are first-class objects.
# This means that
