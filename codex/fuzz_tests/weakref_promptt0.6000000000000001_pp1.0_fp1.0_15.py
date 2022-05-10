import weakref
# Test weakref.ref() and weakref.proxy()

class Foo:
    pass

def callback(r):
    print("deleted", r)

r = weakref.ref(Foo(), callback)
p = weakref.proxy(Foo())
#p = weakref.proxy(Foo(), callback)


# In[ ]:


# Use weakref.WeakValueDictionary
import weakref

class Foo:
    pass

d = weakref.WeakValueDictionary()
d["foo"] = Foo()


# In[ ]:


# Use weakref.WeakKeyDictionary
import weakref

class Foo:
    pass

d = weakref.WeakKeyDictionary()
d[Foo()] = "foo"


# In[ ]:


# Use weakref.WeakSet
import weakref

class Foo:
    pass

s = weakref.WeakSet()
s.add(Foo())


# In[ ]:


# Use weakref.finalize
import weakref

class Foo:
    pass

def callback(r):

