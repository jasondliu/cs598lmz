from types import FunctionType
list(FunctionType(lambda x: x, {}).__globals__)

# get the global variables, which are stored in a dictionary
def f(x):
    return x

g = f.__globals__
g

# change a global value
g['f'] = lambda x : x**2
f(3)

# change a local value
f.__defaults__ = (3,)
f()

# add a global value
g['g'] = lambda y : f(y)
g['g'](2)

# change the code of the function
f.__code__ = f.__code__.__class__(0,0,0,0,"return 'hello'",(),(),(),'','',1,'',())
f()

# change the function name
f.__name__ = 'h'
f
h

# change the function docstring
f.__doc__ = 'hello world'
f.__doc__

# change the module name
f.__module__
f.__module__ = '__main__'
f

# change the closure

