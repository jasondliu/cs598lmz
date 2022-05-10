import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.weak=weakref.proxy(a,callback)
print id(a.weak)
keepali0e.append(lst[0])
del lst[0]
del a
keepalive=a
</code>
Prints the same id. So I have a proxy to a dead object.
<code>&gt;&gt;&gt; a.weak
&lt;__main__.A object at 0x7f48f3ea7f50&gt;
&gt;&gt;&gt; print a.weak.c
&lt;__main__.A object at 0x7f48f3ea7f50&gt;
&gt;&gt;&gt; print a.weak.weak
&lt;__main__.A object at 0x7f48f3ea7f50&gt;
&gt;&gt;&gt; print a.weak.weak.weak
&lt;__main__.A object at 0x7f48f3ea7f50&gt;
&gt;&gt;&gt;
</code>
... and
