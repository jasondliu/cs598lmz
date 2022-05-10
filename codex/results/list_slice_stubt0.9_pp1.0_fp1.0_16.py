import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
b=A()
lst.append(lst)
del lst
ref=weakref.ref(a)
ref2=ref()
a.a.b=ref2.c
lst = [a,ref(),callback,a]
keepalive.append(lst)
print(len(lst))
del a
keepalive.clear()
print(len(lst))
print(lst)
gc.collect()
print(len(lst))
print(lst)
gc.collect()
print(len(lst))


# In[23]:


keepalive=[]
import gc,weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
b=A()
lst.append(lst)
del lst
ref=weakref.ref(a)
ref2=ref()
