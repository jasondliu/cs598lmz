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
I have turned the keepali0e list into a weakref list (call callback on any list item that is deleted) and I have created a object that has reference to itself (A.c=a). Then I have started to delete [:], only the first item can't be deleted, why? A.c should have been collected at this point, right?
Am I missing something here?


A:

target object is weakly referenced by a number of objects so it can't be collected.
Reference Cycle Detection algorithm

