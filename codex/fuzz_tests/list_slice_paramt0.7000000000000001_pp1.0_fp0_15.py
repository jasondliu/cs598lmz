import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
for x in lst:
    print x
</code>
With the code above, I expected the result to be:
<code>&gt;&gt;&gt; 
</code>
However, it actually prints:
<code>&gt;&gt;&gt; ""
</code>
So I guess the reference <code>a.c</code> is not considered as a reference to <code>a</code> by the <code>weakref</code> module.
How can I get rid of the reference <code>a.c</code> inside <code>a</code>?
NB: The real problem is more complicated, but the only relevant part is the reference <code>a.c</code> inside <code>a</code>.


A:

<blockquote>
<p>How can I get rid of the reference a.c inside a?</p>
</blockquote>
Use <code>del a.c</code>

