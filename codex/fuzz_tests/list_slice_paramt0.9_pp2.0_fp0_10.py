import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while keepali0e:print(keepali0e[0]())
print(lst)
#They print:
#<__main__.A object at 0x00000000022EDFD0>
#None
#['"']

#Note that in contrast to the first example, the output does not include an address for the callback. This is becausethe object a has gone out of scope, and we are referencing it only through the callback. The next time the garbagecollector scans the heap, a will have no references, the garbage collector will collect it, the callback will execute,the list element’s reference count will drop to zero, it will be collected, and finally so will the string.

#Finally, note that this requires that the GC keep a list of objects to call the callback on, even after they have been deleted. In the current implementation, this is simply the _deletion_q , which is a part of gc._suitable_for_ref_callback . For an interesting discussion on this, their respective implementations in Python 2.7.3 and the implications for concurrent garbage collection, see http://mail.
