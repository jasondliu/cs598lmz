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
The above code will cause <code>Segmentation fault</code> in Python2.7.6, but works well in Python3.3.3.
I want to know what's the reason behind this.


A:

A <code>Segmentation fault</code> means that the program is trying to access an invalid memory address. In this case, it happens because the <code>str()</code> object is being freed while it is still being used.
When the <code>str</code> is freed, the memory address it is stored at becomes available for use by Python again. When you do <code>lst[:]</code>, it picks up a new <code>str</code> object and stores it at the same address as the old one. But the <code>weakref</code> callback is still using the old address, so it's trying to free memory that is already free.
In Python 3.x, the garbage collector is much smarter, and it won't allow a <code>str</code> object to be freed while it's still in use.

