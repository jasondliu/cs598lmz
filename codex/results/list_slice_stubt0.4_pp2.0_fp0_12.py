import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
wr=weakref.ref(a,callback)
del a
print wr()
print lst
</code>
The output is :
<code>&lt;__main__.A object at 0x7f4d4c4e9c10&gt;
['', &lt;__main__.A object at 0x7f4d4c4e9c10&gt;]
</code>
I think the <code>wr</code> should be <code>None</code> because the <code>a</code> has been deleted.
So why is that?


A:

The <code>a</code> has been deleted, but the <code>a.c</code> still exists.
<code>a.c</code> is a reference to <code>a</code>, so <code>a</code> is still "alive" (i.e. has a reference).

