from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['<lambda>']

# The following is a function that takes a function as an argument and returns a function.
# It is a higher-order function.
def higher_order_function(f):
    def inner():
        print('before')
        f()
        print('after')
    return inner

# The following is a function that takes no arguments and returns nothing.
def function_without_arguments():
    print('function_without_arguments')

# The following is a function that takes one argument and returns nothing.
def function_with_one_argument(a):
    print('function_with_one_argument', a)

# The following is a function that takes two arguments and returns nothing.
def function_with_two_arguments(a, b):
    print('function_with_two_arguments', a, b)

# The following is a function that takes three arguments and returns nothing.
def function_with_three_arguments(a, b, c):
    print('function_with
