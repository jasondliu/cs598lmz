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
print (len(keepali0e))
</code>
this script works.the length of keepsafe is 8.
i want to know why the <code>weakref.ref(a,callback)</code> is alive.
Thanks.


A:

"this script works.the length of keepsafe is 8."
because
<code>while lst:keepali0e.append(lst[:])
</code>
runs
<code>keepali0e.append(lst[:])
</code>
8 times.
Lets look at the mechanics of this.  

you create an object, <code>A</code>
you create a <code>weakref</code> to it and stash it in <code>keepali0e</code>
you add a <code>c</code> attribute to A and set it to <code>a</code> (i.e. itself, forming a cycle)
you delete <code>a</code>, but the <code>weakref</code> in <code>keepali0e</code> prevents <code>A</code> from being
