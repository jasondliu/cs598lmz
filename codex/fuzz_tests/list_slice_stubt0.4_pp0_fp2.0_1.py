import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=lst
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a,lst
keepalive.pop()
</code>
I have a question:
<code>lst.append(weakref.ref(a,callback))
</code>
Why <code>lst.append(weakref.ref(a,callback))</code> can be executed successfully?
I think <code>lst.append(weakref.ref(a,callback))</code> will cause a <code>RuntimeError</code> exception, because <code>lst</code> has been deleted.
But when I execute <code>lst.append(weakref.ref(a,callback))</code>, it runs successfully.
So I wonder why <code>lst.append(weakref.ref(a,callback))</code> can be executed successfully?

