import types
types.MethodType(sum1, 2)

# Create a function that takes a function and two optional arguments and returns a new function which is the result of calling the original function with the optional arguments.

def add_optional_args(function, optional_arg1=None, optional_arg2=None):
    if optional_arg1 == None and optional_arg2 == None:
        def new_func(arg1, arg2):
            return function(arg1, arg2)
    elif optional_arg1 != None and optional_arg2 == None:
        def new_func(arg1, arg2):
            return function(arg1, arg2, optional_arg1)
    elif optional_arg2 != None and optional_arg1 == None:
        def new_func(arg1, arg2):
            return function(arg1, arg2, optional_arg2)
    else:
        def new_func(arg1, arg2):
            return function(arg1, arg2, optional_arg1, optional_arg2)
    return new_func
