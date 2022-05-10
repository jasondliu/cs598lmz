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
del lst
gc.collect()
</code>
But I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;stdin&gt;", line 5, in callback
IndexError: list assignment index out of range
</code>
What am I doing wrong?


A:

The problem is that the callback is called twice, once for each reference you created. The first time it is called, the list is empty and the second time it is called the list is empty.
You can see the problem if you do the following.
<code>import gc
import weakref
class A(object):pass
def callback(x):
    print "callback called"
    del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref
