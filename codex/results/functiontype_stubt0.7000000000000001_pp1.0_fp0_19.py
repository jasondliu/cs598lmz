from types import FunctionType
a = (x for x in [1])
type(a)

# In[ ]:

b = (1 for x in [1])
type(b)

# In[ ]:

c = (lambda x:x for x in [1])
type(c)

# In[ ]:

d = (x for x in [1] if x)
type(d)

# In[ ]:

e = (1 if x else x for x in [1])
type(e)

# In[ ]:

f = (FunctionType(lambda x:x,globals()) for x in [1])
type(f)

# In[ ]:

g = ((lambda x:x)('x') for x in [1])
type(g)

# In[ ]:

h = ((FunctionType(lambda x:x,globals()))('x') for x in [1])
type(h)

# In[ ]:

i = ((x for x in [1]))
type(i)

# In[ ]:

j = ((x for
