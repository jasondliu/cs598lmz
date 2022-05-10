import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
weakref.finalize(str(), callback, lst)
</code>
I get this result:
<code>&gt;&gt;&gt; del lst[0]
&gt;&gt;&gt; del lst[0]
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
IndexError: list index out of range
</code>
I would like to know what is the reason and what is the right way to do it.

