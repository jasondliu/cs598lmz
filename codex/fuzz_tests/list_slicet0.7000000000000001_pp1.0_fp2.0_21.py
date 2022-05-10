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
I know that the problem is in <code>lst</code>, but I don't know how to fix it.
Context: I'm trying to make a tuple with weak references inside.

