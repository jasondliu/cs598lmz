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
Using this script all of my python stuff don't run ("python" causes an empty error message box to appear and disappear) - I can't react to the console because it crashes immediately and the entire system is stuck until I hard reboot it.


A:

Looks like your list cannot be freed until your <code>A</code> instance is removed from memory.
Try cleaning up your reference in the <code>str()</code> callback as well as when you delete <code>a</code>, and see if your problem goes away. You probably don't want to do that on the ref itself within the callback, but rather on the thing the ref refers to.
Note that your script isn't finished. It'll almost certainly crash in the event loop after a few thousand iterations if your strategy is to keep adding to the list and hoping for the best.

