import types
types.FunctionType
# this is FunctionType (aka the type of functions) in Python 2.7;
# there is no FunctionType in Python 3,
# so this Python 2 import is not portable to Python 3

# both may be imported as 'callable' in Python 3:
types.FunctionType
types.LambdaType


# Example
callable(print)       # True; prints are callable (object of type 'builtin_function_or_method'
callable(lambda x: x) # True; lambda expressions (and other functions not imported) are callable
callable(callable)    # True
callable(print.__repr__)  # True
callable(print.__str__)   # True

callable(None)         # False; None is not callable
callable('a')          # False; any object of type 'str' is not callable
callable(complex(1,1)) # False; objects of type 'complex' are not callable

callable(1)            # TypeError; __call__ not defined on int; Python3.5: TypeError
call
