import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.c=None
del a
gc.collect()
print(lst)
keepalive.clear()
keepalive=[]
gc.collect()
print(lst)
