import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=callback
a.e=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(a.c.d)
keepali0e.append(a.e)
del keepali0e[:]
del a
del callback
del lst
