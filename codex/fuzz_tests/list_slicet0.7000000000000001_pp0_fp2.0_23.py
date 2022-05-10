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
Here, <code>a</code> is placed in the <code>keepalive</code> list, so as long as <code>keepalive</code> is alive, <code>a</code> will be alive. As a result, the cyclic reference will be alive until <code>keepalive</code> is alive.
However, the <code>a.c=a</code> line is not what makes the cycle. The cycle is actually the <code>a=A()</code> line (because <code>A</code> inherits from <code>object</code>, which is an instance). The <code>a.c=a</code> line just adds an extra reference to <code>a</code>, but the cycle is still there.

