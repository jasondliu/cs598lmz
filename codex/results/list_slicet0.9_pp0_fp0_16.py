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
Shouldn't <code>del a</code> delete that A object too?
<code>keepali0e</code> looks like this:
<code>[[&lt;weakref at 0x7f60b62db118; dead&gt;], [], [], [], [], [], [], [], ...]
</code>
Am I reading this wrong?


A:

<code>[&lt;weakref at 0x7f60b62db118; dead&gt;]</code> means that the object has been deleted. It's just not removed from the list yet.
The behavior you're seeing is called the "weakly reachable" phase. Once A is garbage collected, the weak reference to A gets called and removed from keepalive list.

