import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
keepali0e.append(callback)
del a,lst,callback
</code>
So I'm wondering how to avoid this, so I can use <code>gc.collect()</code> without worrying about losing data.
Is there a way to stop the garbage collector from deleting an object?

