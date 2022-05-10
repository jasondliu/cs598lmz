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
This creates a cycle of objects, a <code>weakref</code> to one of them, and a <code>list</code> that keeps it alive. Then, when the weakref is destroyed, it deletes the first element of the list. This is what happens:
<code>&gt;&gt;&gt; del a
&gt;&gt;&gt; lst[0]
''
&gt;&gt;&gt; lst
[str()]
&gt;&gt;&gt; keepali0e.append(lst[:])
&gt;&gt;&gt; lst
[]
&gt;&gt;&gt; keepali0e
[[], []]
</code>
The list is empty, but it still is in the <code>keepalive</code> list. If we had a reference to the empty list, it would be detected, but if we don't, the empty list survives.

