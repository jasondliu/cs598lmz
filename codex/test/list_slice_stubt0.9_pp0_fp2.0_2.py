import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
b=A()
keepali0e.append(b)
a.b=b
b.a=a
keepali0e.append(b)
ref=weakref.ref(a,callback)
del a
