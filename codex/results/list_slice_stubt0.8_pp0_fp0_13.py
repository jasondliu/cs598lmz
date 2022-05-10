import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[a,a.c]
print weakref.getweakrefcount(str())
print weakref.getweakrefcount(a)
print weakref.getweakrefcount(a.c)
wr=weakref.ref(a,callback)
print wr
print wr()
print weakref.getweakrefcount(a)
print weakref.getweakrefcount(a.c)
print weakref.getweakrefcount(str())
print weakref.getweakrefcount(str())
del a
print wr()
