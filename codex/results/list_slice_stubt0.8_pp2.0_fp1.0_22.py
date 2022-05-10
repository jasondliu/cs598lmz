import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
del a
del a.c
gc.collect()
</code>
And here's the situation I have now.
As far as I know, the <code>keepali0e</code> list should be empty after garbage collection.
<code>&gt;&gt;&gt; len(keepali0e)
2
</code>
As a result, the size of <code>weakrefable</code> list should be 0.
<code>&gt;&gt;&gt; len(gc.get_objects())
1698
</code>
And I have no idea why this is happening.
<code>&gt;&gt;&gt; gc.get_referrers(lst[0])[0].popitem()
(&lt;weakref at 0x7f09b80f6c10; to 'A' at 0x1e49a10&gt;, 'c')
</code>
Does anyone know why the <code>weakrefable</code> list is not
