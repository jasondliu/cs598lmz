import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
a.d=lst
a.e=callback
keepali0e.append(a)
del a
del keepali0e
del lst
