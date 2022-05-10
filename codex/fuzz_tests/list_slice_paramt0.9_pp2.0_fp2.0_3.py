import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
assert delattr(a,"c")
</code>
fail again.
Is it a bug of python?
How to debug this issue?

