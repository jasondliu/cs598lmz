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
The above line is the one with the error:
<code>del lst[0]
</code>
Any help would be greatly appreciated.


A:

You are deleting <code>lst[0]</code> in the callback. However, this is exactly the value that is being iterated over in the line <code>while lst: keepali0e.append(lst[:])</code>.
You are asking Python to iterate over an array, and delete the first element of that array, at the same time.
This is not supported.

