import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])</code>
<blockquote>
<p>RuntimeError: maximum recursion depth exceeded</p>
</blockquote>
Is there a way to delete an object in the callback?


A:

No, you can't delete an object in a weakref callback.
<code>del</code> is a statement and cannot be used inside a function. What you can do is set an attribute of the object to <code>None</code>:
<code>def callback(x):
    x.c = None
</code>

