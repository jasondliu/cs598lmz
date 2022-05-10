import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
print len(lst)
print len(keepali0e)
</code>
The result is <code>1</code> (as expected) and <code>0</code> (not as expected).
Why does the <code>weakref.ref</code> callback not get called?


A:

The problem is that an object is only weakly referenced if all references to it are weak.  In your case, you have a strong reference to <code>a</code> via <code>keepalive</code>, so <code>a</code> is never garbage collected, and the callback is never called.

