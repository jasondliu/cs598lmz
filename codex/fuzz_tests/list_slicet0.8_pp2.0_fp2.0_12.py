import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:]);del lst[0]
</code>


A:

That's probably impossible :)
This is what happens (on Python 2.7):
On the first <code>del lst[0]</code> a PendingCall does get inserted into the <code>keepalive</code> list, but this PendingCall is never called.
The second <code>del lst[0]</code> is called from a <code>PendingCall</code> that is already in the <code>keepalive</code> list.
This means that you can never break the cycle, as a <code>PendingCall</code> never gets inserted at the start of the <code>keepalive</code> list.

