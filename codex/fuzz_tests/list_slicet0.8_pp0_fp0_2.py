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
del keepali0e
lst


# In[10]:


# Example 01
import weakref
class A(object):pass
def callback(x):print("Removing",x)
a=A()
a.c=a
wk=weakref.ref(a,callback)
del a
wk()


# In[11]:


# Example 02
import weakref
class A(object):pass
def callback(x):print("Removing",x)
a=A()
a.c=a
wk=weakref.ref(a,callback)
del a
wk()
a=[str()]
b=[wk,a]
del b
del a
wk()


# In[12]:


# Example 03
import weakref
class A(object):pass
def callback(x):print("Removing",x)
a=A()
a.c=a
wk=weakref.ref(a,callback)
del a
wk()
a=[str()]
b=[wk,a]
del b
del a
del wk
wk


# In
