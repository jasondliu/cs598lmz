import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a_wr=weakref.ref(a,callback)
keepalive.append(a_wr)
</code>
I would like to know if the garbage collector would delete <code>a</code> or not.


A:

<blockquote>
<p>I would like to know if the garbage collector would delete a or not.</p>
</blockquote>
Not only the garbage collector.
executing your code snippet in the interactive interpreter makes a disappear immediately.
<code>&gt;&gt;&gt; import gc
&gt;&gt;&gt; gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)
&gt;&gt;&gt; gc.set_threshold(0)
&gt;&gt;&gt; class A(object):pass
... 
&gt;&gt;&gt; def callback(x):del lst[0]
... 
&gt;&gt;&gt; keepali0e=[]
&gt;&gt;&
