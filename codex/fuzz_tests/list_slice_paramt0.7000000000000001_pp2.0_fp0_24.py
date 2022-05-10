import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print len(lst)
del a
print len(lst)
</code>
Seems like the callback is not called?
What's the problem?


A:

<code>a.c = a</code> creates a strong reference to <code>a</code>, and the <code>weakref</code> is never called.
You can delete the strong reference by doing:
<code>del a.c
</code>
and then the <code>weakref</code> will be called.

