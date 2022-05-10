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
print len(keepali0e)
print keepali0e
</code>
The output is:
<code>1
[['\x00\x00\x00\x00\x00\x00\x00\x00']]
</code>

