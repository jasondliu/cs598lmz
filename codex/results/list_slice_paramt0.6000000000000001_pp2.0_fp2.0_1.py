import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst
</code>
The following is my understanding of the above codes:

<code>a.c=a</code> creates a circular reference of <code>a</code>.
<code>a</code> is a weak reference to <code>A()</code>, which is set to call <code>callback</code> when <code>a</code> is deleted.
<code>del a</code> deletes the reference to <code>A()</code> and <code>a</code> is set to <code>None</code>.
Since <code>a</code> is set to <code>None</code>, the weak reference of <code>A()</code> is deleted and the <code>callback</code> is called.
<code>callback</code> deletes the first element of <code>lst</code> which is <code>str()</code>.

However, the <code>lst</code> is still filled with <code>str()</code> after the <code>del a</code>.
I thought that the weak reference of
