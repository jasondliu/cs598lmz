from types import FunctionType
list(FunctionType())


# In[ ]:


def f():
    pass

list(f.__code__)


# In[ ]:


for i in f.__code__:
    print(i)


# In[ ]:


def f():
    pass
f.__code__.co_argcount


# In[ ]:


def f(a):
    pass
f.__code__.co_argcount


# In[ ]:


f.__code__.co_nlocals


# In[ ]:


f.__code__.co_varnames


# In[ ]:


f.__code__.co_stacksize


# In[ ]:


f.__code__.co_names


# In[ ]:


def f():
    b = 1
    a = "a"
    c = 1.5
    print(a, b, c)

f.__code__.co_names


# In[ ]:


def f():
    print("f")
    def g
