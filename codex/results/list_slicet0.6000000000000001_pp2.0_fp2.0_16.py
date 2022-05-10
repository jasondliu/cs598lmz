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
print len(keepali0e)
</code>
As you can see, the weakref callback is called after the deallocation of a, but the object is still alive.
Note that the problem doesn't appear with python 2.7.3 or CPython 3.3.0.
Edit: I'm using Python 2.7.4 on Windows 7 64bits.
Edit2: I'm using PyPy 1.9.0 on Windows 7 64bits.


A:

The problem comes from the fact that the <code>PyObject</code> structure is not always allocated as a single block.
In the case of the <code>str</code> object, the structure <code>PyObject</code> is allocated, but the data it points to is not. Instead, the data is allocated in a separate block of memory.
The GC is only aware of the <code>PyObject</code> structure and not the data it points to. So it assumes that the string is already freed when the <code>PyObject</code> structure is freed.
This is probably due to the fact that the string is considered to be immutable.
This behavior is also present
