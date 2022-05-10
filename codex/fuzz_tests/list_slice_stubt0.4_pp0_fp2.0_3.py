import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=callback
del lst
import gc
gc.collect()
</code>
It is not a good idea to use <code>weakref</code> in this way, but it is a way to make the object unreachable.

