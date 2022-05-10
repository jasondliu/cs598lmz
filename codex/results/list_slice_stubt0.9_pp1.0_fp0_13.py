import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive()
lst[0]=a
weakref.ref(lst,callback)
del a,lst
