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
import gc
gc.collect()
print lst

#weakref.WeakKeyDictionary()
#weakref.WeakValueDictionary()
#weakref.WeakSet()
#weakref.finalize()
#weakref.proxy()
#weakref.ref()
#weakref.ReferenceType
#weakref.getweakrefcount()
#weakref.getweakrefs()
