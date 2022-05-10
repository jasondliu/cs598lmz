import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepalive.append(a)
del a
gc.collect()
print(len(lst))
lst.append(weakref.ref(lst,callback))
print(len(lst))
del lst
gc.collect()
print(len(keepalive))
