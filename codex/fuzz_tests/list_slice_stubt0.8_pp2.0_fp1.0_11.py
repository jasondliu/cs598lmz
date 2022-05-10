import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(a))
while lst:pass
print "exiting"
</code>


A:

Consider the following code:
<code>keepalive = []
lst = [str()]
a = A()
a.c = a
lst.append(weakref.ref(a, callback))
lst.append(weakref.ref(a))

while lst:
    pass
</code>
As the <code>while</code> loop runs, the list <code>lst</code> is kept alive by the reference in <code>keepalive</code>. But the only item in <code>lst</code> is a <code>str()</code> that does nothing.
The first item in <code>lst</code>, however, is a <code>weakref</code> that holds a reference to your <code>A</code> instance. As long as <code>lst</code> is alive, that reference is kept alive, and the <code>
