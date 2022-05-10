import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
a.b=weakref.ref(a.c,callback)
a.b()
del a
lst[0]
