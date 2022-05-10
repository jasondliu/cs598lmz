import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
print lst
</code>
I have tried to find out the reason, but it seems that there are no more references to a, so I don't understand why the callback function is not called.


A:

You have a cycle in your object graph, which prevents the objects from being garbage collected.
<code>a = A()
a.c = a
</code>
<code>a</code> references <code>a.c</code>, and <code>a.c</code> references <code>a</code>, so neither <code>a</code> nor <code>a.c</code> can be garbage collected.
You can use the <code>gc</code> module to break the cycle, which will make the objects eligible for garbage collection.
<code>import gc

gc.collect()
</code>

