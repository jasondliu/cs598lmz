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
</code>
This is a simple example of a circular reference.
<code>a</code> has a reference to itself.
<code>lst</code> has a reference to <code>a</code>.
<code>a</code> has a reference to <code>lst</code>.
This is a circular reference.
<code>lst</code> has a weak reference to itself.
When <code>lst</code> is deleted, the weak reference is called, and then the weak reference is deleted.
Now, <code>a</code> has a reference to <code>lst</code>, but <code>lst</code> is deleted.
This is a dangling reference.
When the interpreter exits, it prints a warning about the dangling reference.
I have a question about the warning.
<code>Exception ignored in: &lt;weakref at 0x7f8b0a0b7c78; to 'list' at 0x7f8b
