import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
</code>
The del lst[0] is never called.
I can't figure out why.


A:

The problem is that <code>a</code> has a reference to itself via <code>a.c</code>.  That means that it is kept alive.  The <code>weakref</code> is created on <code>a</code>, but <code>a.c</code> keeps <code>a</code> alive.  The <code>weakref</code> is never called.
If you change the code to:
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=None
keepali0e.append(weakref.ref(a,callback))
del a
</code>
then the callback is called.

