import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:pass
</code>
It seems that <code>a.c</code> is not delete by GC because <code>a</code> is still alive.
So, is there a way to force delete <code>a.c</code>?
Or, is there a way to detect the <code>a.c</code> is a circular reference?


A:

You can not force the cyclic garbage collector to collect a reference cycle.
However, you can easily break the cycle (and can even do it automatically):
<code>import weakref

class A(object):
    def __del__(self):
        self.c = None

a = A()
a.c = a
</code>

