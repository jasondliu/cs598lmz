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
This script is an attempt to show that the <code>__del__</code> function of the object <code>a</code> is called. But the output is:
<code>[[&lt;weakref at 0x7f6a812d55e8; dead&gt;], [''], ['']]
</code>
So it seems the <code>__del__</code> function is not called.
I think I understand why the <code>__del__</code> function is not called. But then how can one show the <code>__del__</code> function is called?


A:

You're not calling <code>__del__</code>; you're calling <code>callback</code>.  <code>callback</code> is called because the weakref you added to <code>keepali0e</code> is cleared when <code>a</code> is deleted.

When you write <code>weakref.ref(a, callback)</code>, you're creating a weakref to <code>a</code> that will call <code
