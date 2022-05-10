import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
c=A()
c.a=a
c.b=callback
a.a=c
keepalive.append(a)
print(lst)
del a,c
print(lst)
