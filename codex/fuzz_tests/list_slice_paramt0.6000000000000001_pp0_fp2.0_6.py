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
gc.collect()
</code>
I do not understand why there is still an object of type <code>A</code> after the garbage collection.
I also tried:
<code>import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.c.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(a.c.c,callback))
del a
del keepali0e
gc.collect()
</code>
In this code, the <code>A</code> object is collected...
What is happening?


A:

<code>keepali0e</code> is still alive, and it contains a
