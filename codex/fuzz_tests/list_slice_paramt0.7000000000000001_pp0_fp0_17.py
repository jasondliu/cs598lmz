import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del lst
del keepali0e
keepali0e
</code>
<code>Output:
[&lt;weakref at 0x000001D5E7E646C8; to 'A' at 0x000001D5E7E64828&gt;]
</code>

