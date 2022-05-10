import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
del a
del lst
a=A()
a.c=a
keepali0e.append(a)
gc.collect()
del a
</code>
When I run this code, I get the error <code>Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in &lt;bound method A.__del__ of &lt;__main__.A object at 0x10a7197f0&gt;&gt; ignored</code>.
I understand that this line of code:<code>del a</code> (delete a) will trigger <code>__del__(self)</code> method in <code>a</code> and in that method, <code>a.c</code> (which is another reference to <code>A</code>)will remove itself, but <code>a.c=a</code> is a circular reference for <code>a</code> and I don't know the reason why <code>a.c.c</code> is not this circular reference when I
