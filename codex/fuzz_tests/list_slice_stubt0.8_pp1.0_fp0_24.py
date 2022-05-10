import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[]
lst[0]='A'*100000000
for ii in xrange(1,100):
    a=A()
    a.c=a
    keepalive.append(weakref.ref(a,callback))
#print sys.getrefcount(a)
</code>
The question is, why is it so hard to get the interpreter to release some memory?  I know that using weak references can let the garbage collector reclaim some of the memory, but how do I force the garbage collector to free up the memory?  Is there some way to force the garbage collector to free up some memory?


A:

You are looking for the memoryview object.  I can't post code because I don't have an example at hand, but give it a try.

