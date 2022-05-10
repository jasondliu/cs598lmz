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
gc.collect()
#result:lst=[str()]
</code>
I want to understand why the evaluation of <code>while lst:keepali0e.append(lst[:])</code> prevents lst from deletion by callback.


A:

You need to call gc.collect() again after the while loop:
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
gc.collect()
gc.collect()
</code>

