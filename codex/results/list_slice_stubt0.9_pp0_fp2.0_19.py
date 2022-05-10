import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.l=lst
lst[0]=a
keepalive.append(a)
print len(lst)
b=A()
b.a=a
weakref.ref(b,callback)
del b
print len(lst)
gc.collect()
lst.append(lst)
print len(lst)
del a
gc.collect()
print len(lst)
