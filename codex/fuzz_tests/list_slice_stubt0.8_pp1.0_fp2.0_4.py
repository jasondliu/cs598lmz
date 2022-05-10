import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepalive.append(a)
lst.append(weakref.ref(lst,callback))
</code>


A:

First of all, I don't think CPython has any particular implementation of weakref.pyc. That's because, as you know, it's implemented in C.
Second, I think I know what is going on here. Let me try to explain it, but it's really difficult to explain.
When you call <code>weakref.ref(lst, callback)</code>, it creates an object (say, <code>wr</code>) which has a reference to the list <code>lst</code>. CPython tracks references between objects and GCs them when they are not needed anymore. <code>lst</code> has a reference to this <code>wr</code>, so <code>lst</code> is not garbage collected. So, if you have a <code>weakref</code> to something that has a reference to you, neither of you will be garbage collected.
Because of this, you can introduce a cycle by creating an object <code>a</code>
