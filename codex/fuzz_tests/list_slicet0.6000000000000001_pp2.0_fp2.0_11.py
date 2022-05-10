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
I would like to know why it happens and how to prevent it. I am using Python 2.7.3.


A:

This is a known bug in Python 2.7.3.  You can use <code>delattr</code> instead of <code>del</code> to delete the attribute <code>c</code> on <code>a</code>.

