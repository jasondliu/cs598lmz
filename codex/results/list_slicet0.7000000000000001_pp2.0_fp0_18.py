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
But it is still not an infinite loop, because lst is eventually populated with a string.


A:

It's not really a loop at all. It's just a bunch of references to a single object.

