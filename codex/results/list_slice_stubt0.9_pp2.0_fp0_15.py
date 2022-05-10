import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del A,objc
</code>
First of all, why is the reference count 5 instead of 3?
Moreover when I add <code>del a</code> in the end then it becomes 3, but if I add <code>lst=[]</code> in the end it becomes 4.
What is going on?


A:

Actually the reference count was 3 before you added the call to <code>callback()</code>, because <code>weakref.ref(obj, callback)</code> increases the reference count on <code>obj</code>. From the docs:
<blockquote>
<p>If given, <em>callback</em> is called with no arguments when the weak
  reference ceases to be valid, that is, when an object is garbage
  collected, or when a referenced object is changed so that the weak
  reference is no longer valid.</p>
<p><em>callback</em> is called whether or not the weak reference has a live reference to the target object.</p>
<p><em>callback</em> can be any callable Python object. The
