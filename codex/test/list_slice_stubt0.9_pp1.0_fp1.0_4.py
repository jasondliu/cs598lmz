import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.c.c=a
lst[0]=a
wr=weakref.ref(a,callback)
lst[0]=None
