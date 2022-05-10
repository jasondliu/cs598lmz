import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a=0
lst[0]=a
weakref.ref(lst[0],callback)
a=None
print 'ok'
</code>
it is ok on python2.7, but on python3.5, an error occurs.
the error info is 
<blockquote>
<p>reference to 'A' not weakly referenced
  object: 0x0000020E3BED6A88</p>
</blockquote>
I think the error is caused by the line a.c=a, but I don't understand why.
help me, please.


A:

<code>lst</code> contains a strong reference to <code>a</code>, so this causes <code>a</code> to be strongly referenced.
You can avoid this by using <code>del</code>.
<code>&gt;&gt;&gt; del lst[0]
&gt;&gt;&gt; gc.collect()
0
&gt;&gt;&gt; gc.collect()
0
</code>
