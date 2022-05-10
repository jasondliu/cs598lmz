import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
lst.append(a)
del a
c=gc.collect()
print(c)
print(lst)
print(keepali0e)

lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
lst.append(a)
del a
c=gc.collect()
print(c)
print(lst)
print(keepali0e)

lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
lst.append(a)
del a
c=gc.collect()
print(c)
print(lst)
print(keepali0e)
