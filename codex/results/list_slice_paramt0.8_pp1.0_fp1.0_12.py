import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
b=A()
lst.append(b)
keepali0e.append(weakref.ref(b))
del lst[0]
b.c=a
alst=weakref.weakref(lst,callback)
