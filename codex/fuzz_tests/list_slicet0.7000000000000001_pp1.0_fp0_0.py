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
I still cannot get it to work.
The only way I can get it to work is to use a list of lists and a for loop, but why does the following not work?
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:lst[:]
</code>


A:

You "should" be able to use a slice assignment, but it's an implementation detail. In CPython, the <code>del list[:]</code> is optimized because the resulting list is just a new wrapper around the same list. So the current list object is still kept alive by the reference in <code>lst</code> and the reference in <code>keepali0e</code>.
If you're using CPython, you'd have to use <code>lst[:] = []</code> for it to work.

