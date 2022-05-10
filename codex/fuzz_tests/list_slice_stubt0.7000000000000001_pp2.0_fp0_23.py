import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wr=weakref.ref(a,callback)
print wr() is a
print wr()
print wr() is a
del a,wr
print lst
print len(keepalive)
</code>
And the output:
<code>True
&lt;__main__.A object at 0x0000000003D865C0&gt;
True
['\x00\x00\x00\x00\x00\x00\x00\x00']
1
</code>
Yes, the weakref is still bound to the object itself, and it's the only object in <code>keepalive</code>, so the only object in the circle.  On the other hand, the <code>list</code> item pointed to by the weakref is no longer accessible from Python, having been replaced by a str of length 8.
<code>a=A()
a.c=a
keepalive.append(a)
a.c=None
keepalive.remove(a)
wr=weakref.ref(a,callback)
</
