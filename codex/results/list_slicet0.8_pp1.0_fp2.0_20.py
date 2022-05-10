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

UPDATE:
Check out http://bugs.python.org/issue17077
<blockquote>
<p>I've been playing with your program on various Python versions and
  platforms, and it seems that this is what's happening here. On my
  Linux box the current master branch, I get:</p>
<pre><code>&lt;code&gt;&amp;gt;&amp;gt;&amp;gt; keepalive = []
&amp;gt;&amp;gt;&amp;gt; lst = [str()]
&amp;gt;&amp;gt;&amp;gt; a = A()
&amp;gt;&amp;gt;&amp;gt; a.c = a
&amp;gt;&amp;gt;&amp;gt; keepalive.append(weakref.ref(a, callback))
&amp;gt;&amp;gt;&amp;gt; del a
&amp;gt;&amp;gt;&amp;gt; len(lst)
1
&amp;gt;
