import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
del a
del lst
lst=None
a=A()
keepali0e.append(a)
lst=[]
keepali0e.append(lst)
weakref.finalize(a,callback,lst)
del a
