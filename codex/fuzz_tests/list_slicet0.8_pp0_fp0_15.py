import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])


# In[ ]:


import weakref
class Example(object):
    def __init__(self):
        self.a=self
        self.b=self
        self.c=self
        self.d=self


# In[ ]:


import weakref
class Example(object):
    def __init__(self):
        self.a=self
        self.b=self
        self.c=self
        self.d=self


# In[ ]:


import weakref
class Example(object):
    def __init__(self):
        self.a=self
        self.b=self
        self.c=self
        self.d=self


# In[ ]:


import weakref
class Example(object):
    def __init__(self):
        self.a=self
        self.b=self
        self.c=self
        self.d=self


# In[ ]:


import weakref
class Example(object):
    def __init__(self):
        self.a=self

