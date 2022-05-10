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
print keepali0e
</code>
I think that the problem is that Python cannot keep the reference to the object after the callback has been run.
The second example is from here:
<code>import gc
import weakref
class A(object):pass
def callback(x):print 'callback'
def f():
    x=A()
    x.c=x
    x.r=weakref.ref(x,callback)
    del x
    return x
gc.disable()
f()
gc.collect()
gc.enable()
print gc.collect()
</code>
And the output is:
<code>&gt;&gt;&gt; 
callback
0
</code>
I think that the problem here is that the callback is not run in the same generation as the object is created.
The third example is from here:
<code>import gc
import weakref
class A(object):pass
def callback(x):print 'callback'
def f():
    x=A()
    x.c=x
    x.r=weakref.ref(x
