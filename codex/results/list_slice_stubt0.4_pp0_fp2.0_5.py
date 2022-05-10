import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)
</code>
I expect the output to be:
<code>['', &lt;weakref at 0x7f7d5b8c8f88; to 'A' at 0x7f7d5b8c8f60&gt;]
['', None]
</code>
But the actual output is:
<code>['', &lt;weakref at 0x7f7d5b8c8f88; to 'A' at 0x7f7d5b8c8f60&gt;]
[]
</code>
Why does the callback not get called?


A:

The problem is that the callback function is never called, because the weak reference is not dead.
The weakref module documentation says:
<blockquote>
<p>... if the referent is still alive, the callback will be invoked with the weak reference object as its only argument. The callback is invoked when the weak reference object is about
