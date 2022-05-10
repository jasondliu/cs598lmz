import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a.c
del a
keepalive.pop()
lst.append(a)
lst.append(weakref.ref(a,callback))
del lst
gc.collect()
print('ok')
