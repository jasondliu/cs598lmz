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
I'm not sure if this is a bug or not.
I'm using Python 2.6.6 on Windows 7.


A:

It's a bug in Python 2.6.6. 
The problem is that the callback function is called twice. 
The first time, the callback function is called when the <code>a</code> object is deleted.
The second time, the callback function is called when the <code>a.c</code> object is deleted.
This is a bug because the callback function is supposed to be called only once.
The bug is fixed in Python 2.7.

