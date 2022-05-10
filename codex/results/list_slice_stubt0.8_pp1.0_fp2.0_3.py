import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a # cycle
a.x=weakref.ref(a,callback)
#keepalive.append(a)
print("before")
del a
print("after")
</code>
I expect the callback to be called and the list lst to be deleted but the callback is not called and lst is still there. What am I doing wrong ?


A:

The line <code>print("after")</code> is causing the issue. Try commenting it out and you'll see that your callback will be called.
This is because when you execute <code>print("after")</code>, you are "activating" your cycle and the garbage collector will not really run.

By using
<code>&gt;&gt;&gt; gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_UNCOLLECTABLE)
&gt;&gt;&gt; gc.collect()
gc: collectable &lt;class 'weakref'&gt; objects: 3
gc: collectable &lt;class 'A'&gt; objects: 2
gc: collectable &lt;class 'str'
