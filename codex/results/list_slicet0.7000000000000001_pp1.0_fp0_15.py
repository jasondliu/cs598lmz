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
Note that this does not solve the problem:
<code>del a.c  # no effect
</code>
It appears that the circular reference is not detected until the weak reference callback is called.
I would like to know what the correct solution is.

