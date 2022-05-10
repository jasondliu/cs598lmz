import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print keepali0e
</code>
Output:
<code>[[&lt;weakref at 0x7f5f5c0b7f80; to 'A' at 0x7f5f5c0b7f50&gt;], []]
</code>

