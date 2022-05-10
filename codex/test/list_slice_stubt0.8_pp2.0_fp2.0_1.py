import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepali0e.append(a)
keepali0e.append(lst)
a.a=a
a.b=a
del a
aa=len(lst)
a=lst[0]
a.a=a
a.b=a
del a
lst[0]=1
lst[0]=''
lst=1
