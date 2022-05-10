import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.w=weakref.ref(a,callback)
del a
del keepalive
print(lst)
</code>
I expected that the list will be empty, but it is not.
Why?


A:

You are creating a reference cycle, which means that the <code>A</code> instance will never be garbage collected.
The <code>weakref.ref</code> object is a proxy to the original object, and it will be garbage collected (and the callback called) when the object is garbage collected. But the object is not garbage collected because of the reference cycle.

