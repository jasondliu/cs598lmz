import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepali0e.append(a)
keepali0e.append(a.b)
keepali0e.append(a.c)
keepali0e.append(lst)
del a
