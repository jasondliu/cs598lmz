import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
</code>
I've tried removing the <code>keepalive</code> list, but it didn't help. I've also tried using <code>weakref.finalize</code>, but that didn't help either. I've tried using <code>objgraph</code> to find out what's keeping the object alive, but I can't seem to find anything.


A:

The problem is that you create a reference cycle with <code>a.c = a</code> which can't be collected by the garbage collector.

