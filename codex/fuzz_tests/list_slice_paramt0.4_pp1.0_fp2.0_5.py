import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)
</code>
I do not understand why the list is not empty.


A:

You are deleting the wrong element.
<code>del lst[0]</code> deletes the first element of the list, but the list has only one element.
You want to delete the list itself: <code>del lst</code>

