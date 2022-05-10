import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del a
print(lst)
</code>
This is the result:
<code>['\x00']
</code>
The <code>callback</code> function is not triggered.
What is wrong?


A:

I'm not sure what you're trying to do, but the problem with your code is that you're creating a reference cycle, which Python's garbage collector ignores.
<code>&gt;&gt;&gt; import gc
&gt;&gt;&gt; gc.set_debug(gc.DEBUG_LEAK)
&gt;&gt;&gt; class A(object): pass
... 
&gt;&gt;&gt; a = A()
&gt;&gt;&gt; a.c = a
&gt;&gt;&gt; gc.collect()
gc: uncollectable &lt;A 0x7f6aab7aa7d0&gt;
gc: uncollectable &lt;A 0x7f6a
