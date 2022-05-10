import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=callback
keepalive.append(a)
keepalive.append(lst)
del keepalive
gc.collect()
print lst
