import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(lst)
keepalive.append(callback)
lst[0]=callback
del keepalive
lst[0]=callback
del lst
import gc
gc.collect()
</code>


A:

The <code>del</code> statement is just a plain old Python statement, and so has no real effect on the execution of the program.  It's just there for the convenience of the programmer.  It doesn't change the way the program runs, so it doesn't change the way the garbage collector runs.
The <code>del</code> statement removes a name from a namespace, but it does not affect the object it refers to.  The garbage collector will only collect an object if there are no references to it.  If there are no references to it, then it doesn't matter whether the name still exists or not.  In fact, it's possible for a reference to an object to exist while there are no names referring to it.  For example, the following code will cause the object <code>x</code> to be garbage collected:
<code>x =
