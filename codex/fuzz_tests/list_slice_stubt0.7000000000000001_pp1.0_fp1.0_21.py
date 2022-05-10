import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(a.c)
lst.append(lst)
lst.append(weakref.ref(lst,callback))
keepali0e.append(lst)
</code>
I'm confused. 
<code>&gt;&gt;&gt; a=A()
&gt;&gt;&gt; a.c=a
&gt;&gt;&gt; lst.append(a)
&gt;&gt;&gt; lst.append(a.c)
&gt;&gt;&gt; lst.append(lst)
&gt;&gt;&gt; lst.append(weakref.ref(lst,callback))
&gt;&gt;&gt; keepali0e.append(lst)
&gt;&gt;&gt; keepali0e
[['', &lt;__main__.A object at 0x03E6A490&gt;, &lt;__main__.A object at 0x03E6A490&gt;,
