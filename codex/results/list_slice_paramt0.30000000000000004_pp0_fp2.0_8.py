import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
gc.collect()
print(lst)
</code>
I expected the output to be <code>[]</code>, but the output is <code>['']</code>.
I am using Python 3.4.3 on Windows 7.


A:

The problem is that the <code>weakref</code> module does not support weak references to cyclic objects.
<code>&gt;&gt;&gt; import weakref
&gt;&gt;&gt; a = []
&gt;&gt;&gt; a.append(a)
&gt;&gt;&gt; weakref.ref(a)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: cannot create weak reference to 'list' object
</code>
The documentation for <code>weakref.ref</code> says:
<blockquote>
<p>
