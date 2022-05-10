import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.c.c=a.c
print lst,'--1'
del lst
print lst,'--2'
a=A()
a.b=1
print hasattr(a,'b'),'--3'
a.b=100
print a.b,'--4'
print getattr(a,'b'),'--5'
print getattr(a,'b','am i?'),'--6'
setattr(a,'b','china')
print a.b,'--7'
print hasattr(a,'b'),'--8'
delattr(a,'b')
print a.b,'--9'
a=A()
print a.__class__.__dict__['__mro__'][-1].__weakref__,'--10'
a.__class__.__dict__['__mro__'][-1].__weakref__=(None,)
print a.__class__.__dict__['__mro__'][-1].__weakref__,'--11'
a.__class__.__dict__['__mro__'
