import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]='abc'
print a.c.c
del a
print lst
del lst
print keepali0e
</code>
when i run this code, the ouput is:
<code>abc
[]
[&lt;weakref at 0x7f1f80d6c3b0; dead&gt;]
</code>
i know the reason is the a.c=a, so the reference count of a is not 0, so it will not be deleted, but the question is, if i change <code>a.c=a</code> to <code>a.c=1</code>, the output will be:
<code>abc
[]
[]
</code>
the element in <code>keepali0e</code> is also deleted, why?

