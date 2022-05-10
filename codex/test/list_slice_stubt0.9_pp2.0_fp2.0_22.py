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
