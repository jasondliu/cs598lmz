import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepalive.append(a)
keepalive.append(lst)
lst[0]=a
print(len(lst))
del a
del lst
print(len(keepalive))
"""

#weakref.ref(obj, callback, *args, **kw)
#weakref.proxy(obj, callback, *args, **kw)
#weakref.getweakrefcount(obj)
#weakref.getweakrefs(obj)
#weakref.WeakKeyDictionary()
#weakref.WeakValueDictionary()
#weakref.WeakSet()

#weakref.WeakMethod(method)
#weakref.finalize(obj, callback, *args, **kw)
#weakref.finalize(obj, callback, *args, **kw)

#weakref.ref(obj, callback, *args, **kw)
#weakref.proxy(obj, callback, *args, **kw)
