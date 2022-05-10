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
You will see that the <code>callback</code> function is called 4 times - which is not what I expected. 
Moreover, I noticed that <code>callback</code> is called only once if I add <code>del</code>s before the <code>keepali0e.append(...)</code>:
<code>import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:
    del keepali0e[0]
    keepali0e.append(lst[:])
</code>
So my question is: why does the garbage collector need to collect items more than once? Is it because it can't always collect items in a single pass? If so, is there any way to force it to take only one pass?


A:

There is no way to force the garbage collector to take only one pass.
What
