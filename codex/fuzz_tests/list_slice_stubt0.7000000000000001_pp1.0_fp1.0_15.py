import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepalive.append(a)
del a
for i in xrange(1000):
    gc.collect()
</code>
If you want to discuss the code itself, go to:
Why can't I delete this object?


A:

The problem is that your <code>callback</code> is not called because the <code>__del__</code> of the <code>str()</code> object is not called.
<code>str</code> implements <code>__del__</code> but if you take a closer look at the C code you see that it is only called if the string is entirely made of ASCII characters and doesn't contain any <code>\0</code> character.

