import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
weakref.ref(a,callback)
lst=[]
a.c=None
keepalive.append(a)
del a
gc.collect()
if lst:print("test passed")
else:print("test failed")
