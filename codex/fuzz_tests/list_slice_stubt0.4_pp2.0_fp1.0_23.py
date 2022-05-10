import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.c=lst
keepalive.append(lst)
del a
del keepalive
gc.collect()
lst[0]='hello'
print lst
del lst
gc.collect()
