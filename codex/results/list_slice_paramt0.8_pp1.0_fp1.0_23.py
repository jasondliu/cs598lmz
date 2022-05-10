import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
</code>
I get the following output:
<code>&gt;&gt;&gt; a.c=1
&gt;&gt;&gt; keepali0e
[&lt;weakref at 0x0000000009BC0C08; to 'A' at 0x0000000009BC2DD8&gt;]
</code>
I am wondering why the <code>callback</code> is not called ? 
I guess it is something I don't understand with the <code>keepalive</code> list ? 


A:

The problem is that the callback requires a change in <code>a</code> itself, so that the weak references will see it as expired. Replacing a child object in <code>a</code> won't do that:
<code>&gt;&gt;&gt; a.c = 1
</code>
In this case, the weak references in <code>keepalive</code> still point to an object that is alive, so the callback isn't called. If you want to use the callback in this case, you'll have to reference
