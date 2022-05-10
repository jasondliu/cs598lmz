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


A:

The problem is that you list contains a reference to <code>a</code>, so it can't be deleted:
<code>&gt;&gt;&gt; a = A()
&gt;&gt;&gt; lst = [a]
&gt;&gt;&gt; del a
&gt;&gt;&gt; lst
[&lt;__main__.A object at 0x104e306d0&gt;]
</code>
To fix this, perhaps use the <code>id</code> of <code>a</code> in your list:
<code>&gt;&gt;&gt; a = A()
&gt;&gt;&gt; id(a)
4540492808
&gt;&gt;&gt; lst = [id(a)]
&gt;&gt;&gt; del a
&gt;&gt;&gt; lst
[4540492808]
</code>

