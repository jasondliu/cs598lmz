import types
# Test types.FunctionType
#
# Create a function that returns the name of the function
#
#   def return_name(func):
#       return func.__name__
#
# Then create a function that returns True if the function name
# is 'return_name' and False otherwise
#
#   def is_return_name(func):
#       pass


def return_name(func):
    return func.__name__


def is_return_name(func):
    if return_name(func) == 'return_name':
        return True
    else:
        return False


# Test types.LambdaType
#
# Create a function that returns True if the function is a lambda function
# and False otherwise
#
#   def is_lambda(func):
#       pass


def is_lambda(func):
    if type(func) == types.LambdaType:
        return True
    else:
        return False


# Test types.GeneratorType
#
# Create a function that returns True if the function is a generator function
# and False otherwise
#
#   def
