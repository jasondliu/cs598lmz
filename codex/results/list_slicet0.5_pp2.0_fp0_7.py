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
<code>[&lt;weakref at 0x7f7e9a9cdbd8; dead&gt;, ['']]
</code>
As you can see, the list is still there.
I would expect that the list is deleted too, because of the callback.
What am I doing wrong?


A:

The callback is called when the <code>A</code> object is finalized.  The <code>A</code> object is not finalized until the reference cycle is broken.  The <code>A</code> object is part of a reference cycle, so it is not finalized.

