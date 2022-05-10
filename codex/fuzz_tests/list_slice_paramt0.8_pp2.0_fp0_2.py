import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))

del a
del a.c
del keepali0e

lst
</code>
Why both object are already released before calling the callback?


A:

It's a little late to respond, but I think I can contribute something to this.
In Python 3.2, a weak reference to an object that contains a reference to itself is not deallocated until the refcount to the object reaches 1.  I speculate that this is because the weak reference to the object itself is the only reference to it and it will get cleaned up when the weak reference is deleted.  In 3.3, this behavior no longer exists.
Here is a demonstration:
<code>&gt;&gt;&gt; import weakref
&gt;&gt;&gt; import sys
&gt;&gt;&gt; class A(object):
...     def __init__(self):
...         self.a = self
... 
&gt;&gt;&gt; a = A()
&gt;&gt;&gt;
