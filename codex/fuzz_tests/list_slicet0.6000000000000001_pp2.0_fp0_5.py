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
The above code produces an overflow error, while the code below does not:
<code>import weakref
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
Note that the only difference between the two codes is the <code>a.c=a</code> line.
Why does the first code produce an overflow error, and the second one does not?


A:

The problem is that in the first case, <code>a</code> is a cyclic reference, which means that it will never be deleted. The reason for this is that the garbage collector will only handle a reference if it is referenced by something that is not part of the cycle. In this case, <code>a</code> is referenced by <code>a.c</code>, which is referenced by <code>a</code>, and
