import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
print len(lst)
</code>
What is the reason for this?


A:

You are creating a reference cycle in the following code
<code>a=A()
a.c=a
</code>
<code>a.c</code> will refer to <code>a</code> and <code>a</code> in turn has a reference to <code>a.c</code>. This cycle will make it impossible for the garbage collector to know whether there is any process that is using the object <code>a</code>. So the garbage collector will not be able to destroy the object <code>a</code> and the object <code>a.c</code> until the program exits.

