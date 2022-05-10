import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print lst
del a
print lst

#print '\n'.join(dir(weakref))
#print weakref.getweakrefcount(a)
#print weakref.getweakrefs(a)
#print weakref.proxy(a)
#print weakref.ref(a)
#print weakref.ref(a,callback)
#print weakref.WeakKeyDictionary()
#print weakref.WeakKeyDictionary(a)
#print weakref.WeakValueDictionary()
#print weakref.WeakValueDictionary(a)
#print weakref.WeakValueDictionary(a,callback)
#print weakref.finalize(a,callback)
#print weakref.finalize(a,callback,a)
#print weakref.finalize(a,callback,a,a)
#print weakref.finalize(a,callback,a,a,a)
#print weakref.finalize(a,callback,a,a,a,a
