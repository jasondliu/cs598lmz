import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))
del a
keepali0e.append(weakref.ref(lst[0]))
while keepalive:keepalive.pop()
</code>
Note that this is a very contrived example, I have just been experimenting with weakrefs and I have no idea if this code is doing what I think it is doing.
EDIT:
I know this is happening because python uses reference counting. I just don't know how to prevent it from happening.


A:

You can't.  You have a circular reference.  The reference counts for all objects involved in the cycle will never go to zero.  You can add <code>del a.c</code> to the end of your example to break the cycle, or you could use a <code>weakref.WeakKeyDictionary</code> instead of a regular <code>dict</code>.

