import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
</code>
the callback function is not called.
<code>&gt;&gt;&gt; import gc
&gt;&gt;&gt; gc.collect()
0
&gt;&gt;&gt; lst
['abc']
</code>
I know it is related to reference cycle, but I still don't understand why the callback function is not called.
<code>&gt;&gt;&gt; a.c
&lt;__main__.A object at 0x7f0d6d7e6b50&gt;
&gt;&gt;&gt; del a
&gt;&gt;&gt; gc.collect()
0
&gt;&gt;&gt; lst
['abc']
</code>
I also know that the callback function is called after I delete the variable <code>a</code>. But why?


A:

<blockquote>
<p>I know it is related to reference cycle, but I still don't understand why the callback function is not called.</p>
</blockquote>

