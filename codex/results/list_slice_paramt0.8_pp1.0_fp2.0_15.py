import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
b=a
keepalive.append(b)
del a
b.c=str()
del b
print(gc.collect())
</code>
This is the output:
<code>2
</code>
Not 0.
Note that Python 3.2+ uses a separate key called <code>__garbage__</code> to allow the garbage collector to know that there are still references pointing to a frame.
That is why Python 3.2+ uses 2 objects in the example above.
For Python 3.3 it prints 0.
So maybe this is a bug. I'm looking at the source code but it's hard so I cannot find anything right now.

