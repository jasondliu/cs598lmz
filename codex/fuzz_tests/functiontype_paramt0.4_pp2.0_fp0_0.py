from types import FunctionType
list(FunctionType(lambda x: x**2, globals(), 'square')(i) for i in range(5))

# A lambda function can be used wherever a function is required,
# such as in the list comprehension above.

# Lambda functions can also be used with the map and filter functions;
# see Built-in Functions.

# The lambda's general form is:
# lambda argument_list: expression

# The argument list consists of a comma separated list of arguments
# and the expression is an arithmetic expression using these arguments.
# You can assign the function to a variable to give it a name.
# The following example uses a lambda expression to return the sum of its two arguments:

f = lambda a, b: a + b
print(f(1, 1))

# The following example uses a lambda expression to return the largest argument:

f = lambda a, b: a if (a > b) else b
print(f(2, 3))

# The following example uses a lambda expression to return True
# if the first argument is divisible by the second:

f = lambda a, b: a % b ==
