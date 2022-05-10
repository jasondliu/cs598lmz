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
</code>
which is the same as the original except for the added <code>del lst[0]</code> in the callback.  This time the reference count of <code>a</code> is 2, the same as it was in the original example.  However, this time <code>a</code> is deleted, because the callback is called before the reference count is decremented.  This is because <code>lst[0]</code> is a string, which is collected immediately, and so the callback is called immediately.

