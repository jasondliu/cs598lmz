from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__()))


# In[6]:


isinstance(a,(str,FunctionType))


# In[7]:


class foo():
    def __init__(self):
        print('class foo __init__')
    def aa(self):
        return 1
    def bb(self):
        return 2
class bar:
    def __init__(self):
        print('class bar __init__')
    def bb(self):
        return 3
class baz(foo,bar):
    pass


# In[8]:


print(baz.mro())


# In[9]:


baz().bb()


# In[10]:


baz().aa()


# # attr 无关继承

# In[11]:


class foo():
    i=1
    def xx(self):
        return 1
class bar():
    x=2
    def yy
