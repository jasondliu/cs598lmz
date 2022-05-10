import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
gc.collect()
print len(lst)
</code>
The output is 1.
The problem is that the <code>a.c</code> is a circular reference, which is not detected by the garbage collector.
In the above example, the reference count of <code>a</code> is 2, and the reference count of <code>str()</code> is 1.
So, the <code>str()</code> object is not garbage collected.
If I use <code>weakref.ref(a)</code> instead of <code>a</code>, the <code>str()</code> object is garbage collected.
Why?


A:

<code>weakref.ref(a)</code> is not a reference to <code>a</code>, it is a reference to a <code>weakref</code> object that will be set to <code>None</code> if the reference count of <code>a</code> goes to zero. 

