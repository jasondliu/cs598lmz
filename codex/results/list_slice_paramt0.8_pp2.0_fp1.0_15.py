import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del lst
</code>


A:

Change your code to:
<code>import gc
import weakref


class A(object):
    pass

def callback(x):
    print 'in callback'
    del lst[0]

keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a

print 'first gc'
gc.collect()

print 'second gc'
del lst
gc.collect()
</code>
You'll see the following output:
<code>first gc
in callback
second gc
in callback
</code>

