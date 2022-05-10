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

import gc
gc.collect()
print keepali0e
</code>
Output:
<code>[&lt;weakref at 0x2c7b0d0; to 'A' at 0x2c7b0f0&gt;, ['\x00'], ['\x00']]
</code>

