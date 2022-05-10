from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))


# In[ ]:


# generator
def gen(n):
    for i in range(n):
        yield n

for i in gen(10):
    print(i)


# In[ ]:


# generator
def gen(n):
    for i in range(n):
        yield n

for i in gen(10):
    print(i)


# In[ ]:


# generator
def gen(n):
    for i in range(n):
        yield n

for i in gen(10):
    print(i)


# In[ ]:


# generator
def gen(n):
    for i in range(n):
        yield n

for i in gen(10):
    print(i)


# In[ ]:


# generator
def gen(n):
    for i in range(n):
        yield
