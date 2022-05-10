import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
gc.collect()
print lst
</code>
The output is
<code>['&lt;callback at 0x7f2f8c1d78c0&gt;']
</code>
Can someone explain the behavior?
I suppose <code>a.c</code> points to <code>a</code>, so when <code>a</code> is deleted, <code>a.c</code> should be <code>None</code>.
<code>a.c</code> should not be referenced by <code>weakref</code>, so <code>a</code> should be garbage collected properly.
Is it because of a bug in python?


A:

When you call <code>del lst[0]</code> in <code>callback</code>, <code>callback</code> itself is being deleted from the weak reference list, so <code>callback</code> is called again and again, until a stack overflow occurs.
You can check this with <code>import traceback; traceback.print_stack()</code>
