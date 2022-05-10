import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
keepali0e.append(lst[0])
del keepali0e
lst[0]=A()
lst[0].c=lst
lst[0].c[0]=lst[0]
lst[0].c[0].c=lst[0].c
del lst
