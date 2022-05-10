import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(a)
keepalive.append(lst)
wr=weakref.ref(a,callback)
keepalive.append(wr)
</code>


A:

When you create a weak reference <code>wr</code> to <code>a</code>, with a callback <code>callback</code>, what you are saying is that

The function <code>callback</code> will be called if <code>a</code> becomes unreachable: this is what happens when A is deleted, in your case.
The function <code>callback</code> will be called with an argument whose value is <code>wr</code>.

In your case, <code>callback</code> deletes <code>lst[0]</code>, which is the empty string. It does not touch <code>a</code> or <code>wr</code>.

