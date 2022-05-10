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
If you're trying to check for GC, why not just use a more direct approach instead of trying to guess from timings?
<code>import gc
lst = [str(), str(), str(), str()]
keepalive = [lst[:]]
del lst[:]
assert gc.collect() == 0
del keepalive[:]
assert gc.collect() == 4
</code>

