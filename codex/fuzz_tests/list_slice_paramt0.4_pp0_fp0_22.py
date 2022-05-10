import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
print lst
</code>
But it doesn't work. The list is still not empty.
I want to know why.
I think it should work.


A:

The problem is that <code>a.c</code> is a reference to <code>a</code> itself, so when you delete <code>a</code>, <code>a.c</code> is also gone.  This means that <code>a.c</code> is no longer in the list <code>keepalive</code>, so the callback isn't called.
You can fix this by making a copy of <code>a</code> before deleting it:
<code>import weakref

class A(object): pass

def callback(x): del lst[0]

keepalive = []
lst = [str()]
a = A()
a.c = a
keepalive.append(weakref.ref(a, callback))
keepalive.
