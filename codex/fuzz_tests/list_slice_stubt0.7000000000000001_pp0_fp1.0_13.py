import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
weakref.ref(a,callback)
b=A()
b.c=b
keepalive.append(b)
lst[0]=b
del b
del a
</code>
I expected 'callback' to be called by python. But it's not. I am using python 2.7 on 64 bit machine.
Any hints on where I am wrong?


A:

You're not holding a reference to anything in <code>keepalive</code> (unless the <code>weakref.ref()</code> call somehow does that). All the references in <code>keepalive</code> go out of scope as soon as the list is created, so the objects are eligible for GC. Try this instead:
<code>keepalive.append(weakref.ref(a))
</code>

