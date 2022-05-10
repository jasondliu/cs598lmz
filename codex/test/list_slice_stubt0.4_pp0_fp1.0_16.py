import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
keepali0e.append(callback)
weakref.ref(a,callback)
del keepali0e
del a
del lst
del callback
