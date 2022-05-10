import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=lst
lst.append(a)
keepali0e.append(a)
lst[0]=str()
del a
del keepali0e
