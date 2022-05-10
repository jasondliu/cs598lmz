import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
</code>
But this does not work:
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
</code>
The second example does not call callback. Why?
(I am asking because I need to keep a weakref to an attribute of an object and I do not want to keep a strong reference to the object itself. Keeping a strong reference would defeat the purpose of weakrefs.)


A:

The callback is called when the object is garbage collected, which it will not be if there's a strong reference to it.
<code>&gt;&gt;&gt; import weakref
&gt;&gt;&gt; class A(object):
...     pass
... 
&gt;&gt;&gt; def callback(x):
...     print "callback called"
... 
&gt;&gt;&gt; keepali0
