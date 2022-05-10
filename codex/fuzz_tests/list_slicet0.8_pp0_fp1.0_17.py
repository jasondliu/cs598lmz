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
print keepali0e
</code>
which is given in the documentation.
The expected output is:
<blockquote>
<p><code>&lt;code&gt;[&amp;lt;weakref at 0x040F9FF0; dead&amp;gt;, [&amp;lt;__main__.A object at 0x040F9F30&amp;gt;]]&lt;/code&gt;</code></p>
</blockquote>
or 
<blockquote>
<p><code>&lt;code&gt;[&amp;lt;weakref at 0x040F9FF0; dead&amp;gt;, []]&lt;/code&gt;</code></p>
</blockquote>
(if the callback is triggered just before the loop, instead of at some point inside the loop).
Instead, what I get is:
<blockquote>
<p><code>&lt;code&gt;[&amp;lt;weakref at 0x023B3F00; dead&amp;gt;, [&amp;lt;__main__.A
