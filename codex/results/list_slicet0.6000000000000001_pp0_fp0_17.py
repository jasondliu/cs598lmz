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
The above code is a modified version of the code in the following link:
http://www.dabeaz.com/python/GIL.pdf
I want to know why the while loop is never terminated. I cannot understand how the reference is kept alive. Can someone help?


A:

I think you are confused about what the code is doing. The reference to <code>a</code> is not kept alive, but the reference to <code>a.c</code> is.
<code>a</code> is held in <code>keepalive</code>, so it does not get deleted. The callback is not called at this point, as <code>a</code> is still alive.
The callback is only called when the last reference to <code>a</code> is deleted. But because <code>a.c</code> is still alive, <code>a</code> is not deleted.
This is called a circular reference, and is a common source of memory leaks in Python.

