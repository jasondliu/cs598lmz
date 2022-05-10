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
The change is simply the second line. I tried this on my computer and the loop is interrupted by a <code>RuntimeError</code> (maximum recursion depth reached).
<blockquote>
<pre><code>&lt;code&gt;RuntimeError: maximum recursion depth exceeded
&lt;/code&gt;</code></pre>
</blockquote>
I think this is because <code>callback</code> is called again and again, deleting the <code>str()</code> object every time but leaving <code>a.c</code> pointing at the same object. The reference count of the string object goes to zero, and then <code>callback</code> is called, and then the string object's reference count go to zero and so on.
This is based on my assumption that Python strings are immutable, so the deletion of the string object does not cause the <code>a.c</code> reference to be altered, but that may be incorrect.
You may have to use a weakly referenced list as in the question to get around this, or you may need to un
