import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
a.b=b
b.b=a
keepali0e.append(a)
keepali0e.append(b)
lst[0]="abc"
