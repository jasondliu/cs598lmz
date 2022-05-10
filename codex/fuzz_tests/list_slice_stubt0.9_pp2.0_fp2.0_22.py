import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a.c
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(a.d)
del a
lst[0]=weakref.ref(A,callback)
del lst
print keepali0e
print
print '=================================================================='
print
keepali1e=[]
class A(object):pass
a=A()
a.c=a
a.d=a.c
keepali1e.append(a)
keepali1e.append(a.c)
keepali1e.append(a.d)
keepali1e.append(A)
del A
del a
print keepali1e
del keepali1e[:2]
print keepali1e
