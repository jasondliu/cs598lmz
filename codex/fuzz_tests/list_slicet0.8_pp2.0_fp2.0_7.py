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
print(keepali0e)
</code>
So when I run this and I expect that the GC runs,
but it doesn't.
Why is it?
How can I run the GC with "weakref"?

