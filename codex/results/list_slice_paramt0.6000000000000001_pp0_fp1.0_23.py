import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del lst[0]
print keepali0e
</code>
It prints
<code>[&lt;weakref at 0x7f4a2b3cd7b0; to 'A' at 0x7f4a2b3cd7e0&gt;]
</code>

