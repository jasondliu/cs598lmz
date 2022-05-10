from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, 'f', f.__defaults__, f.__closure__))

# In[ ]:


# Example:
def f(x, y):
    return x + y

list(FunctionType(f.__code__, f.__globals__, 'f', f.__defaults__, f.__closure__))

# In[ ]:


# Example:
def f(x, y):
    return x + y

list(FunctionType(f.__code__, f.__globals__, 'f', f.__defaults__, f.__closure__))

# In[ ]:


# Example:
def f(x, y):
    return x + y

list(FunctionType(f.__code__, f.__globals__, 'f', f.__defaults__, f.__closure__))

# In[ ]:


# Example:
def f(x, y):
    return x + y

list(FunctionType(f.__
