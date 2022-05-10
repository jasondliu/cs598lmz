import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
lst.append(a)
lst.append(a.c)
keepali0e.append(lst)
keepali0e.append(callback)
print keepali0e
print weakref.getweakrefcount(a)
print weakref.getweakrefcount(a.c)
print weakref.getweakrefcount(lst)
print weakref.getweakrefcount(lst[0])
print weakref.getweakrefcount(lst[1])
print weakref.getweakrefcount(lst[1].c)
print weakref.getweakrefcount(lst[2])
print weakref.getweakrefcount(callback)
wr=weakref.ref(a,callback)
print weakref.getweakrefcount(a)
print weakref.getweakrefcount(a.c)
print weakref.getweakrefcount(lst)
print weakref.getweakrefcount(lst[0])
print weakref.getweakrefcount
