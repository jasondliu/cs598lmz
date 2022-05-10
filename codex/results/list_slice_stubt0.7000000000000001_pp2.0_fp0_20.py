import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=lst
keepalive=a
keepalive=weakref.ref(keepalive,callback)
del a,callback
gc.collect()
print len(lst)
