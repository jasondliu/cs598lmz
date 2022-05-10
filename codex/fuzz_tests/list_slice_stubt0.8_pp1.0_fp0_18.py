import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
a.lst=lst
lst.append(a)
weakref.ref(a,callback)
</code>


A:

As soon as you <code>del lst[0]</code>, the list <code>lst</code> is empty.  An object is only kept alive by a container object so long as it is in the container.  Therefore <code>a</code> becomes eligible for garbage collection, and so does <code>lst</code> (because it no longer contains <code>a</code>).  But then <code>a.lst</code> also becomes eligible for garbage collection, and so on.  Since the <code>a</code> object has a reference to itself, the whole thing goes into an infinite loop of objects being removed from weakrefs and then being eligible for garbage collection.
It's not the callbacks that are "running" - it's just that the objects no longer have any references to them so they are eligible for garbage collection.

