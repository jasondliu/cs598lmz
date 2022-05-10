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
print keepali0e
</code>
The output is:
<code>[&lt;weakref at 0x7f7d4d4e8c30; dead&gt;, ['']]
</code>
So, the <code>callback</code> function is called, and the <code>lst</code> is empty.
But, when I change the <code>lst</code> to a <code>list</code> of <code>A</code>, the <code>callback</code> function doesn't called.
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[A()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print keepali0e
</code>
The output is:
<code>[&lt;weakref at 0x7f7d4d4e8c30; dead&gt;
