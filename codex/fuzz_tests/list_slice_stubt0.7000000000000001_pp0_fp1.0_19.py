import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))
</code>
The output is:
<code>&gt;&gt;&gt; a=A()
&gt;&gt;&gt; keepali0e.append(weakref.ref(a,callback))
&gt;&gt;&gt; keepali0e.append(weakref.ref(a))
&gt;&gt;&gt; del a
&gt;&gt;&gt; lst
['\x00']
</code>
I thought that the output would be:
<code>&gt;&gt;&gt; lst
[]
</code>
Why does the reference not go out of scope?


A:

<code>callback</code> is called when a reference is removed from a <code>weakref.WeakKeyDictionary</code> or <code>weakref.WeakValueDictionary</code>.
In your case, the <code>a</code> is not a key/value in a dictionary,
