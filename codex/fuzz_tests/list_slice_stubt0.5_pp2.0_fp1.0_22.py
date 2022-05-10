import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=a
keepalive0=a.c
keepalive1=lst
keepalive2=callback
keepalive3=weakref.ref(lst[0],callback)
del keepalive,keepalive0,keepalive1,keepalive2,keepalive3
print lst

class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepalive=a
keepalive0=a.c
keepalive1=lst
keepalive2=callback
keepalive3=weakref.ref(lst[0],callback)
del keepalive,keepalive0,keepalive1,keepalive2,keepalive3
print lst

class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepalive=a
keepalive0=a.c
keepalive1=lst
keep
