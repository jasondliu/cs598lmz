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


# In[7]:


import weakref
class A(object):pass
lst=[str()]
del lst[0]
a=A()
a.c=a
del a


# In[8]:


import weakref
class A(object):pass
lst=[str()]
del lst[0]
a=A()
a.c=a
keepa1ive=list(lst)
del a


# In[9]:


import weakref
class A(object):pass
lst=[str()]
del lst[0]
a=A()
a.c=a
keepa2ive=dict(lst=lst)
del a


# In[10]:


import weakref
class A(object):pass
lst=[str()]
del lst[0]
a=A()
a.c=a
keepa3ive=vars()
del a


# In[11]:


import weakref
class A(object):pass
lst=[str()]
del lst[0]
