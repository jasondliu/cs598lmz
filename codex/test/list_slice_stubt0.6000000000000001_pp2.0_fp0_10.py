import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.a=a.b=a
lst.append(a)
lst.append(lst)
keepali0e.append(lst)
keepali0e.append(a)
keepali0e.append(callback)
lst.append(callback)
