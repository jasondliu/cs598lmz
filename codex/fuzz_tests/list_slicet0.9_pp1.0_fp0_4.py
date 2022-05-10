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

<code>$ /opt/pypy-1.9/pypy/translator/goal/pypy-c pypy_ref.py
MemoryError
</code>


A:

It seems that your bug is actually a Feature -- the issue has been logged at
http://bugs.pypy.org/issue1027
<blockquote>
<p>The WeakValueDictionary is used to implement weakref.ref(), because we
  want to be able to call the callback when the last reference to it
  goes away.  This means that it needs to be saved somewhere -- by
  default, it must remain alive.</p>
<p>If you don't use the callback immediately, you can workaround it by
  destroying the callback and saving the data in a temporary spot:</p>
<pre><code>&lt;code&gt;&amp;gt;&amp;gt;&amp;gt; x = []
&amp;gt;&amp;gt;&amp;gt; def foo():
...     y.append(x)
... 
&amp;gt
