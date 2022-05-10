import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=lst
a.a=weakref.ref(lst,callback)
del lst
keepalive[:]
keepalive.append(a)
keepalive[:]
del keepalive
a.a
A.__dict__['c']
del A.__dict__['c']
a.a
A.__dict__['c']=a
a.a
del A.__dict__['c']
a.__dict__['a']
