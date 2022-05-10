import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]
lst[0]

print ('ok')

# the weakref module supports the notion of a weak reference, a handle to an object that does not keep it alive.

# Weak references to an object are not enough to keep the object alive: when the only remaining references to a referent are weak references, garbage collection is free to destroy the referent and reuse its memory for something else.

# A primary use for weak references is to implement caches or mappings holding large objects, where it’s desired that a large object not be kept alive solely because it appears in a cache or mapping.

# In some cases, it is desirable to track objects as long as they are alive, but avoid keeping them alive longer than necessary. The WeakValueDictionary class provides this behavior, using a dictionary that maps keys to weak references to values.

# The following example shows the difference between a normal dictionary and a WeakValueDictionary. The normal dictionary keeps its keys and values alive as long as the dictionary itself is alive:

import weakref
s1={}
s2={}
def bye():
    print('Gone with
