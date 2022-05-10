from types import FunctionType
list(FunctionType(lambda:None).__code__.co_varnames)

# In[ ]:

def f(x):
    y = x + 1
    return y

list(FunctionType(f.__code__).__code__.co_varnames)

# In[ ]:

def f(x):
    y = x + 1
    return y

def g(f):
    return f(1)

list(FunctionType(g.__code__).__code__.co_varnames)

# In[ ]:

def f(x):
    y = x + 1
    return y

def g(f):
    return f(1)

list(FunctionType(g.__code__).__code__.co_varnames)

# In[ ]:

def f(x):
    y = x + 1
    return y

def g(f):
    return f(1)

list(FunctionType(g.__code__).__code__.co_varnames)

# In[ ]:
