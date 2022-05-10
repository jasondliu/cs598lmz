import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepalive.append(lst)
weakref.ref(a,callback)
</code>
I got this from the internet, how does it make a cycle?
I think <code>a.c=a</code> is not a cycle, it's a simple reference. Then <code>lst[0]=a</code> is a reference too.
I don't see any cycle here.


A:

In Python, an object can have multiple references to it.  So, if an object has a reference to itself, that's a cycle.
This is a way to create a cycle:
<code>&gt;&gt;&gt; a = []
&gt;&gt;&gt; a.append(a)
</code>
Now <code>a</code> is a list containing itself.

