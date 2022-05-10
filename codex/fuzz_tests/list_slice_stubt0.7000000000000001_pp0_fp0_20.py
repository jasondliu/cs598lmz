import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
print 1
</code>
And in my opinion, it is the same as:
<code>lst=[str()]
del lst[0]
print 1
</code>
But this time it shows:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    del lst[0]
IndexError: list assignment index out of range
</code>
Just like this:
<code>lst=[str()]
print 1
del lst[0]
</code>
The only different is the order of <code>del lst[0]</code> and <code>print 1</code>.
If <code>del lst[0]</code> is executed before <code>print 1</code>, it shows <code>IndexError: list assignment index out of range</code>.
If <code>print 1</code> is executed before <code>del lst[0]</code>, it shows nothing.
Is this a bug?


A:
