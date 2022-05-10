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
It's important to note that the weakref callback is called in a pretty arbitrary context, so you shouldn't do anything too fancy in the callback.  Normally the callback is run in a context that is similar to a system error handler (general debugging shouldn't be allowed to raise any exceptions, or they'll get caught by the error handler, even if they're just caught and ignored).  However, the implementation of the callback is platform dependent, so you shouldn't trust it to be anything in particular.

