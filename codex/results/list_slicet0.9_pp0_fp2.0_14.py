import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
len(lst)
</code>
It previously was 
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(weakref.ref(a,callback))
del a
while lst:pass
len(lst)
</code>
From the <code>while lst</code> loop, <code>lst</code> is clearly empty. So where does the <code>str()</code> at index <code>0</code> come from? 
I am using <code>Python 3.5.2</code>.
Note that previous to this change, the actual program (which is a bit more complex) was passing the test.


A:

This issue is not a regression or a bug in CPython, nor is it an issue in any other Python implementation.
The <code>weakref</code> documentation is clear (emphasis mine):
<blockquote>
<p>The <code>&lt;code
