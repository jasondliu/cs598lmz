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
del lst
</code>
And the code:
<code>a=A();lst=[a.];del a
n=len(lst)
while len(lst)&gt;=n:keepali0e.append(lst[:])
del lst
</code>
It seems that Python has :

written "collectable" to the internal weakref list's entry and
deleted(recursively?) the memory space holding the <code>a</code> object on Python side
then later when the weakref callback is triggered, it turned out that the object continued to be referenced by <code>a.c</code>
then the object was indirectly referenced by the internal weakref list and can not be deleted

So my question is :
Is this a tenable theory about how Python implements weakref, or this is an extreme pathological case and we shall not concern about such a corner case?


A:

It's not a tenable theory because the C API for weak references does not appear to have any concept of an object being deleted recursively from another object. That code is looking up the object, not just checking
