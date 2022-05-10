import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
lst.append(a)
lst.append(lst)
lst.append(weakref.ref(lst,callback))
lst.append(keepalive)
print lst[0]
print lst[1]
print lst[2]
</code>
What I want to ask is that when I use <code>keepalive</code> to keep a reference to <code>lst</code> after doing the previous steps, <code>lst</code> still can not be GCed. So what exactly is happening in this situation?


A:

The <code>weakref.ref</code> to <code>lst</code> is a dead weakref. As long as <code>lst[2]</code> is referenced, <code>lst</code> is not garbage collected. However, <code>lst[2]</code> is not a weakref object, it's a callable object.
The callable object is a <code>weakref.ReferenceType</code> instance. <code>lst[2]</
