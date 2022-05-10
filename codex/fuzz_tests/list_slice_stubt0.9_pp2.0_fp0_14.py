import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.attr=weakref.ref(a,callback)
lst.append(a)
keepalive.append(a)
</code>
From this point there is a circular reference, <code>a.c</code> pointing to <code>a</code> and <code>a.attr</code> pointing to <code>a.c</code>. When I run this code under Python 2.6.1 I get an segfault, but under 2.5 I get <code>TypeError: can't delete weakly referenced object</code>
I can get over this problem in 2.6.1 by modifying only the first line in the callback
<code>def callback(x):del lst[0]
</code>
to 
<code>def callback(x,lst=lst):del lst[0]
</code>
and now I get the <code>TypeError</code> exception again, but only for the first line in the callback. I can't use this trick when I'm implementing a more sophisticated class with more functions, then I get segfault again. The segfault
