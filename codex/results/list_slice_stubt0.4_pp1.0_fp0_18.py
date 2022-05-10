import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=lst
keepalive.append(a)
keepalive.append(lst)
lst[0]=lst
weakref.ref(lst,callback)
del a
del keepalive
del lst
gc.collect()
</code>

