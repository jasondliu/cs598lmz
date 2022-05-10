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
print keepali0e
</code>
Output:
<code>[&lt;weakref at 0x00E8F3A0; dead&gt;, ['\x00']]
</code>
This is with Python 2.7.3.
Why does that happen? The reference cycle does not contain any global objects, function objects, or class objects. It should be cleared.


A:

Before Python 2.7, the garbage collector didn't collect cycles of objects from global variables.  In Python 3, that behavior changed.  You can do the same thing in 2.7 by disabling the cyclic garbage collector:
<code>import gc
gc.disable()
</code>

