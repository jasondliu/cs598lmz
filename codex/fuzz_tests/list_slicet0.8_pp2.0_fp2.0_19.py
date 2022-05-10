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
[gc.collect() for i in range(3)]
</code>
I am trying to create a circular reference, whose callbacks will be issued, but the callback will be only able to access a list, because as soon as one tries to delete an element from it, it becomes garbage collected.

