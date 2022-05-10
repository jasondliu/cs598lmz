import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
lst[0]=a
lst[0].c=weakref.ref(a,callback)
del a
del keepali0e
