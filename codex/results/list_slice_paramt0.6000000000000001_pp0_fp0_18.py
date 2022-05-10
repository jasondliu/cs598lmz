import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
while lst:
    pass
</code>
This code will hang.
I think this is because <code>weakref.ref</code> would call <code>callback</code> when it is first created and <code>a</code> is not collected yet,so <code>lst</code> is not empty.
But I don't understand why <code>weakref.ref</code> would call <code>callback</code> when it is first created.
Is there any way to make the code work normally?
Thanks!


A:

You're not doing anything wrong, this is a known bug in Python.
The problem is that Python doesn't always call the callback with the object as the first argument; the object is only passed to the callback if the object is still alive.
For example, if you change your code to
<code>keepalive = []
lst = [str()]
a = A()
a.c = a
keepalive.append(weakref.ref(a, callback))
del a
while lst:
    pass
</code>
Then the callback is
