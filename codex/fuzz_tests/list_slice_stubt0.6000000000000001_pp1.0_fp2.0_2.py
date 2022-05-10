import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del a
print lst

#output: []

#A weakref can be created to a class instance with a callback function. The function is called when the instance is about to be destroyed.
#The weakref callback function is called before the instance is actually destroyed, so the instance is still accessible in the callback.
#The weakref callback function can also be used to destroy circular references.

#https://docs.python.org/2/library/weakref.html

#https://docs.python.org/2/library/weakref.html
#A weak reference to an object is not enough to keep the object alive: when the only remaining references to a referent are weak references, garbage collection is free to destroy the referent and reuse its memory for something else.
#A primary use for weak references is to implement caches or mappings holding large objects, where it’s desired that a large object not be kept alive solely because it appears in a cache or mapping.
#The WeakValueDictionary class provides this behavior.

#http://stackoverflow
