import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
keepali0e.append(callback)
del a,lst
gc.collect()
</code>
The problem is that the weakref.ref object is not deleted, and the callback function is not called.
I am using Python 3.4.3, and I have also tried this on Python 2.7.9, and the problem is the same.


A:

You need to keep the <code>weakref.ref</code> object alive too:
<code>import gc
import weakref

class A(object): pass

def callback(x):
    del lst[0]

keepalive = []
lst = [str()]
a = A()
a.c = a
keepalive.append(a)
keepalive.append(a.c)
keepalive.append(lst)
keepalive.append(callback)

# create a weak reference to a, and keep it alive
weakref_
