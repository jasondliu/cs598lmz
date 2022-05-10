import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst.append(weakref.ref(lst,callback))
del lst
print keepalive
</code>
I have tried to run this code in python2.7 and python3.2. But it doesn't work.
I want to know why it doesn't work.
Thanks a lot.


A:

The reason is that the <code>weakref.ref</code> object is not the same as the list object.  The <code>weakref.ref</code> object is a proxy for the list object.  When the list object is deleted, the <code>weakref.ref</code> object is not deleted.  The <code>weakref.ref</code> object is only deleted when the list object is deleted and there are no other references to the <code>weakref.ref</code> object.

