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
print 'end'
</code>
The output is:
<code>[&lt;weakref at 0x02D7E0F0; dead&gt;, []]
end
</code>

