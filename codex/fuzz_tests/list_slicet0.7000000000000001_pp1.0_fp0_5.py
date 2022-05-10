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
There is something that I'm missing with this code, could someone explain?
I'm on python 3.3.3 btw.


A:

In your code <code>del lst[0]</code> removes (deletes) the first element from <code>lst</code>.
In python 3 <code>del</code> is a statement, not a function, so it can't be passed as a callback.

