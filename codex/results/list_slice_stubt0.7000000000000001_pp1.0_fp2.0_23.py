import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
lst.append(str())
</code>
<code>lst[0]</code> does not get deleted, because the reference cycle is not broken.

