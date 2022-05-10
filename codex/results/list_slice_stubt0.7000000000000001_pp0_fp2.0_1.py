import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a,keepalive
for i in xrange(100000): print "*"*100000
</code>
Once the callback is run (by the weak reference being collected) the <code>lst</code> object will be destroyed and the loop will be broken.
The <code>a.c=a</code> is to ensure that the <code>A</code> object is not collected before the loop starts.

