import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=weakref.ref(a,callback)
lst.append(keepalive)
lst.append(keepalive)

del a
#del keepalive
gc.collect()
print lst
