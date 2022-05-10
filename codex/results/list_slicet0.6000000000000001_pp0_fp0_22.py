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
print(keepali0e)
</code>

<code>&gt;&gt;&gt; import weakref
&gt;&gt;&gt; class A(object):pass
... 
&gt;&gt;&gt; def callback(x):del lst[0]
... 
&gt;&gt;&gt; keepali0e=[]
&gt;&gt;&gt; lst=[str()]
&gt;&gt;&gt; a=A()
&gt;&gt;&gt; a.c=a
&gt;&gt;&gt; keepali0e.append(weakref.ref(a,callback))
&gt;&gt;&gt; del a
&gt;&gt;&gt; while lst:keepali0e.append(lst[:])
... 
&gt;&gt;&gt; print(keepali0e)
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '
