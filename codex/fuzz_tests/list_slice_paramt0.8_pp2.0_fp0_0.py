import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
gc.collect()
</code>
As we can see, when an object with a circular reference is weakref'ed (keepalive), its <code>__del__</code> method is not called, even if we collect it with <code>gc.collect()</code>
Why is that?
Thanks in advance for your answers.


A:

<code>__del__</code> is called only when an object looses its reference count.
For this to happen the circular reference has to be resolved. This happens by garbage collection.
As long as you have a circular reference you can't collect it. The weak reference can help in certain situations to break the circular reference. Since the reference to <code>a</code> is weak and not strong, <code>a</code> is not referenced by the weak reference.
The weak reference should resolve the circular dependency and enable the garbage collection.
Now you might think why it is not possible to call <code>__del__</code> without a reference to the instance.
I don't know the explanation, but the instance has no references which means the instance is dead, right
