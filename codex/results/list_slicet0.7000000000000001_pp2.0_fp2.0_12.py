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
print(keepali0e[-1])
</code>
I think the problem is the circular reference. But I don't know how to fix it.


A:

I don't know what you're trying to do here, but the problem is that you are creating a circular reference.  Remove the line <code>a.c = a</code> and it should work fine.

