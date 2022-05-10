import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
callback(a)
del lst
del a
del callback
gc.collect()
print "hello"
print keepalive
</code>
Output:
<code>hello
[&lt;weakref at 0x7fc8a6ac23b8; dead&gt;]
</code>
This example works for me because python does not run cyclic gc for <code>str</code>-objects.

