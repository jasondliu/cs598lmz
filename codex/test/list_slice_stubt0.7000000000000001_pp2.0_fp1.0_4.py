import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
lst.append(A())
lst.append(A())
a=A()
a.c=a
lst.append(a)
lst[-1].c=lst[-1]
