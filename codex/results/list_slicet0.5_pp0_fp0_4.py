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
I got the following output:
<code>[[&lt;weakref at 0x7f1f0d8c4b00; to 'A' at 0x7f1f0d8c4b90&gt;], ['\x00\x00\x00\x00\x00\x00\x00\x00'], ['\x00\x00\x00\x00\x00\x00\x00\x00'], ['\x00\x00\x00\x00\x00\x00\x00\x00'], ['\x00\x00\x00\x00\x00\x00\x00\x00'], ['\x00\x00\x00\x00\x00\x00\x00\x00'], ['\x00\x00\x00\x00\x00\x00\x00\x00'], ['\x00\x00\x00\x00\x00\x00\x00\x00'], ['\
