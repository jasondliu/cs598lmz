import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
print lst
</code>
Why is the <code>callback</code> not called?


A:

<blockquote>
<p>Why is the callback not called?</p>
</blockquote>
The <code>callback</code> is called, and <code>lst</code> ends up empty.
<code>print</code> is executed before the callbacks are called, so <code>lst</code> still contains one element when <code>print</code> is executed and <code>lst</code> is printed.
To see that the callbacks are called, just add some debugging to the <code>callback</code> function:
<code>def callback(x):
    del lst[0]
    print 'Callback called'
</code>
Demo:
<code>&gt;&gt;&gt; import weakref
&gt;&gt;&gt; class A(object):pass
... def callback(x):
...     del l
