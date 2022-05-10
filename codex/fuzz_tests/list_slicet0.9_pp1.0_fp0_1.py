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
import gc
print "gc.get_referents(keepali0e[-1]): ",gc.get_referents(keepali0e[-1])
print "before : keepali0e",keepali0e
keepali0e.pop()
print "after : keepali0e",keepali0e
print "gc.collect() is called"
gc.collect()
print "after gc.collect() : keepali0e",keepali0e
</code>
The last part:
<blockquote>
<pre><code>&lt;code&gt;print "before : keepali0e",keepali0e
keepali0e.pop()
print "after : keepali0e",keepali0e
print "gc.collect() is called"
gc.collect()
print "after gc.collect() : keepali0e",keepali0e
&lt;/code&gt;</code></pre>
<p>The result is: </p>
<pre><code>&lt;code&gt;before : keepali
