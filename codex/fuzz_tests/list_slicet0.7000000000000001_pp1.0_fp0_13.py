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
I know if i comment the last line it will work, but I don't know why it doesn't work without commenting that line.
I get the following error:
<code>RuntimeError: cannot create weak reference to 'str' object
</code>
I wonder if it's because of the way I initialize the list
<code>lst=[str()]
</code>
or because of the way I add new elements to the list
<code>keepali0e.append(lst[:])
</code>
Any help would be appreciated


A:

You can't create weak references to immutable objects. This is documented in the <code>weakref</code> documentation.
Python lists are mutable, but you are creating a list of empty immutable <code>str</code> instances, which you then never change.

