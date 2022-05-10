import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
keepalive.append(a)
del a
lst

#!python
"""
1.weakref.finalize(self, obj, func, *args, **kwargs)

Register a callable to be called when obj is garbage collected.

If a cycle is present which includes obj, the object will be uncollectable
and finalization callbacks will not be called.

The first argument to func will be obj, followed by args and kwargs.

If the weak reference callback is registered for an object more than once,
the callback will be called more than once.

2.weakref.getweakrefcount(object)

Return the number of weak references to object.

3.weakref.getweakrefs(object)

Return a list of all weak reference objects that point to object.

4.weakref.proxy(object[, callback])

Return a proxy object that weakly references object.

The proxy object is callable and has most of the methods of object.

The proxy will only be callable if
