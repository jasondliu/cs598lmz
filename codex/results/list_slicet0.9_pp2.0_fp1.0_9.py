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
print len(keepali0e)/2
</code>


A:

If you want to prevent that from happening, you need to modify CPython to use generation-based garbage collection (sometimes called "tracing garbage collection"). The downside, of course, is then you won't find leaks until the build up to that point could cause memory exhaustion, and it can be difficult to debug. I have seen this option enabled on some embedded systems, though. (Incidentally, even if you are using tracing GC everywhere else, you need to run the tests with reference counting, or you will fail more than half of them.)
Why/How?
Consider the first time a <code>weakref.ref</code> is created: it is a perfectly behaved reference, with no proxy object yet. The only thing that makes it special is that it has a callback; this is just a function to call when the referent is about to die, so there has to be one. But until it does the callback, it is an everyday reference, not a weak one.
And that's the problem: where should it go? The original object is not in any generation, because it's new, and the proxy object doesn't
