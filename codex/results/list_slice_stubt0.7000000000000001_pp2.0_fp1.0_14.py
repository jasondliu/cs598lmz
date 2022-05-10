import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepalive.append(lst)
weakref.ref(a,callback)
</code>
I am trying to understand this piece of code by using gc.get_referrers(a), but I don't understand why when I change the code to:
<code>from gc import get_referrers
from weakref import ref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepalive.append(lst)
ref(a,callback)
</code>
The callback function does not get called and the reference cycle still exists.
EDIT
It seems that I was wrong, the callback function does get called, only not when I call get_referrers(a).


A:

The <code>gc.get_referrers</code> function is implemented as a call to the <code>gc.get_referents</code> function, which gets called by the garbage collector when it is
