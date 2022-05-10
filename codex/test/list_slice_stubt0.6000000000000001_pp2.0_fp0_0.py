import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a.c
a.a=a.b
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(a.b)
keepali0e.append(a.a)
keepali0e.append(str())
a.a=str()
a.b=str()
a.c=str()
a=str()
keepali0e.append(lst)
keepali0e.append(callback)
del keepali0e
lst[0]="a"*(2**31-1)
