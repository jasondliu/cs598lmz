import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[a]
del a
lst.append(A())
keepalive.append(A())
del A
lst.append(str())
keepalive.append(str())
