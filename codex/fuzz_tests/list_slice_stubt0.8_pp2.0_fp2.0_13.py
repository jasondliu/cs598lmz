import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(A())
keepalive=[]
for i in range(16):
    o = A()
    o.c = o
    lst.append(o)
    keepalive.append(o)
keepalive.append(WeakMethod(A().__init__,callback,a))
#del keepali0e,keepali0e,lst
gc.collect()
a=b=c=None
#del a,b,c
