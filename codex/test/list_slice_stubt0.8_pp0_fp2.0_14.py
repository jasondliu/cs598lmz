import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepali0e.append(weakref.ref(lst[0],callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del lst
