import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
print(lst)
lst[0]=weakref.ref(a,callback)
print(lst)
del a
print(lst)
print(keepalive)
keepalive[0].c=None
print(lst)
print(keepalive)

#weakref.WeakKeyDictionary
#weakref.WeakValueDictionary
#weakref.WeakSet
#weakref.finalize
#weakref.proxy
#weakref.getweakrefcount
#weakref.getweakrefs
#weakref.ReferenceType
#weakref.CallableProxyType
