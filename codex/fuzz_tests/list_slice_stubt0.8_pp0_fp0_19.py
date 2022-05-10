import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
A.d=a
keepali0e.append(a)
a.e=a
a.f=lambda :callback(lst)
a.g=lst
del a
gc.collect()
print lst
