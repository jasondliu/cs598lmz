import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
c=A()
c.a=c
a.b=[weakref.ref(A(), callback), lst,
     weakref.ref(c),
     weakref.ref(A(), callback)]
c.b=a.b
