import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a.c
lst.append(a.b)
lst.append(a.c)
keepalive=lst
del lst
f=weakref.ref(a,callback)
del a
f()
</code>
<blockquote>
<p>Exception: ReferenceError: weakly-referenced object no longer exists</p>
</blockquote>


A:

<code>a.b</code>'s reference count is going up, because it's being assigned to <code>lst[1]</code>, so the circular reference isn't broken.
Keepalive entries are also ignored when computing the reference count.
You can remove the keepalive entry by dereferencing it:
<code>keepalive.pop()
</code>

