import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
weakref.ref(lst[0],callback)
del a
del lst
import gc
gc.collect()
print(keepalive)
</code>
I want to know why the object a is not deleted.

