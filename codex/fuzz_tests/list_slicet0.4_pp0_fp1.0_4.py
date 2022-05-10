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
print(keepali0e)
</code>
The output is:
<code>[&lt;weakref at 0x02F7A0F0; to 'A' at 0x02F7A0C0&gt;, ['\x00'], []]
</code>

