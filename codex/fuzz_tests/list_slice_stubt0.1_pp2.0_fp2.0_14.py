import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
lst.append(weakref.ref(lst,callback))
del lst
gc.collect()
print(keepalive)
