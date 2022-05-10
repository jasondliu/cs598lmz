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
This example has the same problem as the previous one, replacing the <code>weakref</code> call with <code>del lst[0]</code> inside <code>callback</code> makes it work.
Why doesn't Python garbage collect the objects that I explicitly tell it to (<code>keepalive</code> and <code>lst</code>) and the object that has a circular reference to itself (<code>a.c</code>)?


A:

Python is implemented with reference counting.  That means that it can only garbage collect objects when the reference count goes to 0, and that obviously doesn't happen for the two lists in your examples, which you keep appending to as long as it doesn't. 

