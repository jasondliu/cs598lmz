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
I've tried to make the example as simple as possible.  I'm using the CPython 2.7.5, and the above code just hangs.  The same code in Python 3.3.2 works as expected and prints <code>[]</code>.  I cannot find any mention of this behavior in the docs.  Is it a bug?

