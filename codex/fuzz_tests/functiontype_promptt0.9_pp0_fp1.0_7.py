import types
# Test types.FunctionType with the "callable" built-in.
def to_callable(f, not_callable=None):
    if callable(f):
        return f
    else:
        return not_callable


# Test types.FunctionType with the "for ... in ..." statement.
def for_in_func():
    for i in range(10):
        yield i


# Test types.FunctionType with the "isinstance" built-in.
def isinstance_func(i):
    if isinstance(i, types.FunctionType):
        return "i is a function"
    else:
        return "i is not a function"


# Test types.FunctionType with "doctests"
def func_for_doctests(): 
   """Returns a function that returns x, for argument x."""
   f = lambda x: x
   return f


# Test types.MethodType, types.ClassType and types.InstanceType
# with "doctests"
def m(): 
    """Returns a method of int"""
    class X:
        def f(self): 
