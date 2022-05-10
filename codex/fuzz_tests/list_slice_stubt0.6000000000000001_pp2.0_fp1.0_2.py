import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
a.b=b
b.b=a
keepali0e.append(a)
keepali0e.append(b)
lst[0]="abc"
print weakref.getweakrefcount(lst[0])
print weakref.getweakrefcount(a)
print weakref.getweakrefcount(b)
print weakref.getweakrefcount(a.b)
print weakref.getweakrefcount(a.c)
print weakref.getweakrefcount(b.c)
print weakref.getweakrefcount(b.b)
print weakref.getweakreflist(lst[0])
print weakref.getweakreflist(a)
print weakref.getweakreflist(b)
print weakref.getweakreflist(a.b)
print weakref.getweakreflist(a.c)
print weakref.getweakreflist(b.c)
print weakref.getweakreflist(b.b)
print weakref.get
