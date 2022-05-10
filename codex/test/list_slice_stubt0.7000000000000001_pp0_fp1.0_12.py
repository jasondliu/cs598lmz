import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepali0e.append(a)
keepali0e.append(str())
keepali0e.append(weakref.ref(a.b,callback))
keepali0e.append(weakref.ref(a.c,callback))
del keepali0e
del a
del lst
