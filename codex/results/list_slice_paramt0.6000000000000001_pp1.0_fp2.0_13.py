import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
</code>
And the output is:
<code>&gt;&gt;&gt; del a
&gt;&gt;&gt; del keepalive
&gt;&gt;&gt; lst
[]
</code>
But it is not what I want. I want to delete <code>a</code> and <code>keepalive</code> is still there.
I want the output is:
<code>&gt;&gt;&gt; del a
&gt;&gt;&gt; del keepalive
&gt;&gt;&gt; lst
['a']
</code>
How can I do it?


A:

The problem is that keeping an object alive doesn't actually keep it alive. As soon as everything that has a reference to the object is destroyed, the object is destroyed. You can't keep an object alive by keeping a reference to it in a list that you then delete.

