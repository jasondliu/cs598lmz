import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=lst
keepalive.append(a)
del a
keepalive.append(lst)
del lst
weakref.ref(lst,callback)
del callback
del keepalive
