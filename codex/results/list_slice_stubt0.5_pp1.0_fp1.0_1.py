import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(a)
weakref.ref(a,callback)
del lst,a
print keepalive
</code>
So, why the <code>del lst</code> not causing the <code>callback</code> to be called?


A:

The key is that the <code>callback</code> is only called when the object itself is garbage collected, not when any of the references to the object are removed. 
The <code>callback</code> is only called when <code>a</code> is garbage collected, and that does not happen until all references to it are gone. 
The <code>del lst</code> statement does not remove any references to <code>a</code>, so it does not cause a call to <code>callback</code>.

