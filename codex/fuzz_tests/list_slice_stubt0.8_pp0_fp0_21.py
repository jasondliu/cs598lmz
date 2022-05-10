import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=a
weakref.ref(a,callback)
keepali0e.append(a)
keepali0e.append(a.a)
keepali0e.append(a.b)
keepali0e.append(a.c)
del(a)
del(a)
del(a)
del(a.a)
del(a.b)
del(a.c)
del(a)
del(a)
del(a)
del(a.a)
del(a.b)
del(a.c)
del(a)
del(a)
del(a)
del(a.a)
del(a.b)
del(a.c)
print(lst)
