import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(a.c,callback))
keepali0e.append(a.c)
del a
del keepali0e
