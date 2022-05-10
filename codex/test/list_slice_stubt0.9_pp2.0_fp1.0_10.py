import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=A()
a.e=a
a.name=a
a.t=A()
a.t.callback=callback
lst[0]=a
