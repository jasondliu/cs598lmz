import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]+='a'
del lst
</code>
<code>callback</code> gets called but <code>del lst[0]</code> within <code>callback</code> ends up deleting the entire list, thus it is no longer callable.
Is there a way I could make the weakref callback issue <code>del lst[0]</code> upon callback?


A:

The problem is that <code>lst[0]</code> is a str, not a list:
<code>&gt;&gt;&gt; type(lst[0])
&lt;class 'str'&gt;
</code>
<code>lst[0]</code> is a string reference to the string. <code>weakref.WeakSet</code> requires that the weakref points to a type that defines <code>__del__</code>. <code>str</code> does not support <code>__del__</code> so <code>weakref.WeakSet</code> refuses to return a weakref
