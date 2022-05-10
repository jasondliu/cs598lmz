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

<code>&gt;&gt;&gt; import weakref
&gt;&gt;&gt; class A(object):pass
...
&gt;&gt;&gt; keepalive = weakref.ref(A())
&gt;&gt;&gt; keepalive.__class__
&lt;type 'weakref'&gt;
</code>

