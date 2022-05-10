import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
del a
while lst:pass
</code>
Or in 2.7 with <code>import gc; gc.collect()</code> at the appropriate place.

In later versions of Python you get a message to tell you what it was:
<code>&gt;&gt;&gt; import weakref
&gt;&gt;&gt; class A(object):pass
... 
&gt;&gt;&gt; def callback(x):del lst[0]
... 
&gt;&gt;&gt; lst=[str()]
&gt;&gt;&gt; lst.append(A())
&gt;&gt;&gt; lst[-1].c=lst[-1]
&gt;&gt;&gt; keepalive=weakref.ref(lst[-1], callback)
&gt;&gt;&gt; del lst[-1]
&gt;&gt;&gt; 
Exception ignored in: &lt;bound method A.__del__ of &lt;__main__
