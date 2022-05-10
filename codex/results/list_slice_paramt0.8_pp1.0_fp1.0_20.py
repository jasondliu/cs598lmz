import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
keepali0e.append(weakref.ref(a,callback))
</code>
this is meant to illustrate somewhat what is going on, the problem is that I can't seem to find a solution to this, so I'm hoping someone with more experience with weakrefs could help me figure out what I'm doing wrong.
Thanks, and sorry for the long post.


A:

I think this is what your code currently does:

<code>a.c = a</code>: <code>c</code> is a strong reference from <code>a</code> to itself.
<code>a = A()</code>: creates a new object <code>a</code>.
<code>a.c = a</code>: <code>c</code> is now a strong reference from <code>a</code> to the old <code>a</code>.
<code>keepali0e.append(weakref.ref(a,callback))</code>: creates a strong reference to <code>a</code>, which means it cannot yet be garbage collected.
<code>del a</code
