import types
# Test types.FunctionType is used to check if the object is a Python function
isFunction = lambda f: isinstance(f, types.FunctionType)

##
# @brief Returns the name of the function.
#
# This method will return the name of the function.
#
# @param f Function instance.
#
# @return Name of the function.
def getFunctionName(f):
    return f.__name__

##
# @brief Returns the function arguments.
#
# This method will return the function arguments.
#
# @param f Function instance.
#
# @return Function arguments.
def getFunctionArguments(f):
    return f.__code__.co_varnames[:f.__code__.co_argcount]

##
# @brief Returns the function default arguments.
#
# This method will return the function default arguments.
#
# @param f Function instance.
#
# @return Function default arguments.
def getFunctionArgumentsDefault(f):
    return f.__defaults__

##
# @brief Returns the function docstring.

