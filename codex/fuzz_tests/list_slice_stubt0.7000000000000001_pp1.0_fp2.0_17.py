import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
a.a=a
keepali0e.append(a)
a.b=a
keepali0e.append(a)
try:
    weakref.finalize(a,callback,lst)
except Exception as e:
    raise RuntimeError from e
gc.collect()
del a
print(lst)

#output:
#['']

#A weak reference, as the name implies, does not keep the referent alive: when the last strong reference to the object is removed,
# the weakly referenced object is automatically removed from the weak reference.
# This can be used to write cache-like structures: the object can remove itself from the cache when the last strong reference is removed.
#It can also be used to implement the Observer pattern (see PEP 318):
# the subject and the observer have weak references to each other to avoid reference loops:
# when the last strong reference to either one is removed, the corresponding object is automatically removed from the other’s weak reference list.

#The module defines the following functions:

#weakref.ref(
