import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del keepali0e
</code>
Does not trigger the callback in those python versions. Note that there is no reference to <code>a</code> anymore, but only to <code>a.c</code>. It seems that the reference to <code>a</code> is kept via the <code>self</code> reference. 
This seemingly happens for all those versions (I tested 2.4 - 3.2). Trying the same thing with a <code>weakref.WeakKeyDictionary</code> instead of the <code>callback</code> function also keeps the reference. 
Here's a workaround I found:
<code>Python 2.7.8 (v2.7.8:ee879c0ffa11, Jun 29 2014, 21:07:35) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt
