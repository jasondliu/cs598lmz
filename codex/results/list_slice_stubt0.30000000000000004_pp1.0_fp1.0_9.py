import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst.append(weakref.ref(A(),callback))
del lst
gc.collect()
print len(keepalive)
</code>
The output is <code>1</code>, which means the <code>weakref</code> has been deleted. But in my case, the <code>weakref</code> is still there.
I have tried to use <code>gc.collect()</code> to force the garbage collection, but it doesn't work.
I have also tried to use <code>gc.disable()</code> and <code>gc.enable()</code> to disable the garbage collection, but it doesn't work either.
I have also tried to use <code>sys.getrefcount()</code> to check the reference count of the <code>weakref</code>, but it is always <code>1</code>.
I have also tried to use <code>sys.getrefcount()</code> to check the reference count of the <code>weakref</code>'s callback, but it is always <code>1</code>.
