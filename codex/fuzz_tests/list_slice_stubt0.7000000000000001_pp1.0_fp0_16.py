import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a.c, callback))
del a
gc.collect()
for i in range(100):lst.append(str())
gc.collect()
