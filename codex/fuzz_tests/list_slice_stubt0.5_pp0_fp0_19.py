import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=a
keepalive=keepalive
keepalive=keepalive
lst.append(weakref.ref(a,callback))
print(len(lst))
del a
del keepalive
gc.collect()
print(len(lst))
