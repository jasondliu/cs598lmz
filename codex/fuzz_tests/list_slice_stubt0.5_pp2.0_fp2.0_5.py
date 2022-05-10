import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
lst[0]=a
lst[0].c=weakref.ref(a,callback)
del a
del keepali0e
</code>
I don't know if it is a bug or i miss something.
edit:
I found out that the problem is that the weakref callback is called even before the gc is called.
Is there a way to delay the callback to the gc call?


A:

I don't know if this is a bug or not, but the problem is that the <code>weakref</code> callback is called even before the garbage collection is called.
You can delay the callback to the gc call by creating a simple wrapper for <code>weakref</code> objects:
<code>import weakref

class WeakRef(object):
    def __init__(self, ref, callback):
        self._ref = weakref.ref(ref, callback)

    def __call__(self):
        return self._ref()
</code>
And then use it like this:
<code>def callback(x):
   
