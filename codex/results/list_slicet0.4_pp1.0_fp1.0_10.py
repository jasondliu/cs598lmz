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
</code>
The code is supposed to run until the list is empty, but it doesn't.
The problem is that the callback function is not called.
I've tried to use <code>weakref.finalize</code> instead of <code>weakref.ref</code> but the result is the same.
I've also tried to use <code>weakref.proxy</code> instead of <code>weakref.ref</code>, but it doesn't work.
I've tried to use <code>weakref.WeakSet</code> instead of <code>weakref.ref</code>, but it doesn't work.
I've tried to use <code>weakref.WeakKeyDictionary</code> instead of <code>weakref.ref</code>, but it doesn't work.
I've tried to use <code>weakref.WeakValueDictionary</code> instead of <code>weakref.ref</code>, but it doesn't work.
I've tried to use <code>weakref.WeakMethod</code> instead of <code>weakref.ref</code>, but it doesn't work.
I've tried to use
