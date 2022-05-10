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
print keepali0e
</code>
It never prints the list.
I tried to use <code>gc.collect()</code> but it doesn't work.
I also tried to use <code>weakref.finalize</code> but it doesn't work either.
I also tried to use <code>weakref.proxy</code> but it doesn't work either.
I also tried to use <code>weakref.WeakSet</code> but it doesn't work either.
I also tried to use <code>weakref.WeakKeyDictionary</code> but it doesn't work either.
I also tried to use <code>weakref.WeakValueDictionary</code> but it doesn't work either.
I also tried to use <code>weakref.WeakMethod</code> but it doesn't work either.
I also tried to use <code>weakref.WeakMethodProxy</code> but it doesn't work either.
I also tried to use <code>weakref.WeakSet</code> but it doesn't work either.
I also tried to use <code>weakref.WeakValueDictionary</code> but it
