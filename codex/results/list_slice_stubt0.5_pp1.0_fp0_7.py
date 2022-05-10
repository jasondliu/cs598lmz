import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
del a
lst=[]
c=weakref.ref(a,callback)
keepalive.append(c)
del keepalive[:]
del c
del lst
</code>
Is this behaviour expected?
Why is it happening?
Is there a way to get around this?


A:

<code>&gt;&gt;&gt; del lst[0]
&gt;&gt;&gt; lst
['', '']
&gt;&gt;&gt; del lst[0]
&gt;&gt;&gt; lst
['']
&gt;&gt;&gt; del lst[0]
&gt;&gt;&gt; lst
[]
</code>

