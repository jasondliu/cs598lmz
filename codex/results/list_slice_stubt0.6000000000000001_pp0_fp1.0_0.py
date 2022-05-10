import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
lst.append(callback)
del lst,a,callback
import gc
for i in range(2):gc.collect()
del keepalive
</code>
But I'm not sure is this a good excuse to call it a bug.

