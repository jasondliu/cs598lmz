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
(The first element of lst is an empty string, which means it will be deallocated when the refcount for that object reaches 0.)
In CPython 2.6, I get the expected result:
<code>&gt;&gt;&gt; import gc
&gt;&gt;&gt; gc.collect()
3
&gt;&gt;&gt; gc.collect()
0
</code>
But in CPython 3.2, I get:
<code>&gt;&gt;&gt; import gc
&gt;&gt;&gt; gc.collect()
1
&gt;&gt;&gt; gc.collect()
1
</code>
I've also tried:
<code>&gt;&gt;&gt; import gc
&gt;&gt;&gt; gc.collect()
1
&gt;&gt;&gt; str()
''
&gt;&gt;&gt; gc.collect()
0
</code>
So, it seems that CPython 3.2 has
