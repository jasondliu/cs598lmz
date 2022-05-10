import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
</code>
I want to get some information about the objects in list <code>lst</code>.


A:

You can use the <code>gc.get_referrers</code> function:
<code>import gc

print(gc.get_referrers(lst))
</code>
Example:
<code>&gt;&gt;&gt; lst = []
&gt;&gt;&gt; gc.get_referrers(lst)
[{'__builtins__': &lt;module '__builtin__' (built-in)&gt;,
  '__name__': '__main__',
  '__doc__': None,
  '__package__': None,
  'lst': []}]
</code>

