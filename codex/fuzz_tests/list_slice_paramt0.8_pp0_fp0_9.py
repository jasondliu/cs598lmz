import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepalive.append(weakref.ref(a.c,callback))
del a
gc.collect()
print lst[0]
</code>
This is an example of creating a cycle where we want the non-circular objects to be deleted and we want the circular objects to be kept alive.  It is intended to simulate the situation where I want to keep a window manager object alive while all its window objects are deleted.  I want to eventually be able to delete the window manager object as well.
The problem is that the circular references are deleted as well.  The addition of the del a line above solves this problem but that is a very hacky solution and I don't understand why it does this.  I have verified that the objects are circular with the code below:
<code>&gt;&gt;&gt; a.c is a
True
</code>
If the comment del a line is uncommented, lst[0] is printed as expected.
For me this behavior is very tricky, since I have a lot of circular references in my code but I only want to make sure that the reference count of an object is not decremented
