from types import FunctionType
list(FunctionType(lambda:0,{}).__code__.co_varnames) 

# ['x']

# Note that this is identical to (but much more efficient than):
#
# def f(x):
#     return x
#
# list(f.__code__.co_varnames)
#
# ['x']


"""
 
 
 """
