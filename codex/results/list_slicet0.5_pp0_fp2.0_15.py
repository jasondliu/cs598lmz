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
import gc
print gc.collect()
</code>
The output is
<code>0
</code>
So the reference cycle is not collected.
Why is that?


A:

The <code>gc.collect()</code> function is not guaranteed to collect all garbage. If there are still strong references to objects in the cycle, it will not collect them.
From the docs:
<blockquote>
<p><code>&lt;code&gt;gc.collect()&lt;/code&gt;</code><br/>
  This function invokes the garbage collector, forcing collection of unreferenced objects. <strong>Note that garbage collection is not guaranteed to occur for every collection of unreferenced objects.</strong> Also, <strong>even when it is invoked, there are no guarantees that it will collect all unreferenced objects.</strong> </p>
</blockquote>

