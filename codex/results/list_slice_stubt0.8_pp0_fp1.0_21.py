import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.i=lst[:]
keepalive.append(a)
callback=weakref.ref(callback,callback)
d={'a':1,'b':2}
del d
lst.append(a)
del lst[1].i
del lst[0],lst[0]
del keepalive[0].i
del keepalive[0].i
del lst
</code>

To understand why this is, it's important to know how Python's garbage collection works. It's actually quite simple. At some point in your program, the reference counter of the object reaches zero and at that point, the object is destroyed. The exact time that this happens is implementation-specific and is typically not something that anyone cares about. The implementation uses some heuristic to figure out when this happens, but that's an implementation detail.
The problem with your question is that you're asking about the time complexity at some time in the program. There's no specific time in the program that you can use. It's not even clear what you mean by "before". The same object that you mean by "after" is the same object that you mean by
