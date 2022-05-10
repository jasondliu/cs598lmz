import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepali0e.append(a)
a.c=keepali0e
lst.append(str())
keepali0e.append(lst)
b=A()
b.c=b
lst[1]=b
keepali0e.append(b)
b.c=keepali0e
del keepali0e
