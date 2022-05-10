import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]
</code>
I have tried to make a weakref to a circular object. But the callback is not called.
I think it's because the object is still referenced.
Is it possible to make a weakref to a circular object?


A:

The object is still referenced by the <code>a.c</code> attribute. If you delete that attribute, the object will be collected:
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
&gt;&gt;&gt
